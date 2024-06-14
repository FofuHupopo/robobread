import hashlib
import json
import types
from uuid import UUID

import requests

from .utils import Encoder
from .models import PaymentModel
from .settings import get_config


class PaymentHTTPException(Exception):
    pass


class MerchantAPI:
    _terminal_key = None
    _secret_key = None
    _success_url = None
    _fail_url = None

    def __init__(self, terminal_key: str = None, secret_key: str = None):
        self._terminal_key = terminal_key
        self._secret_key = secret_key

    @property
    def secret_key(self):
        if not self._secret_key:
            self._secret_key = get_config()['SECRET_KEY']
        return self._secret_key

    @property
    def terminal_key(self):
        if not self._terminal_key:
            self._terminal_key = get_config()['TERMINAL_KEY']
        return self._terminal_key

    @property
    def success_url(self):
        if not self._success_url:
            self._success_url = get_config()['SUCCESS_URL']
        return self._success_url
    
    @property
    def fail_url(self):
        if not self._fail_url:
            self._fail_url = get_config()['FAIL_URL']
        return self._fail_url

    def _request(self, url: str, method: types.FunctionType, data: dict) -> requests.Response:
        url = get_config()['URLS'][url]

        data.update({
            'TerminalKey': self.terminal_key,
            'Token': self._token(data),
        })

        r = method(url, data=json.dumps(data, cls=Encoder), headers={'Content-Type': 'application/json'})

        if r.status_code != 200:
            raise PaymentHTTPException('bad status code')

        return r

    def _token(self, data: dict) -> str:
        base = [
            ['Password', self.secret_key],
        ]

        if 'TerminalKey' not in data:
            base.append(['TerminalKey', self.terminal_key])

        for k, v in data.items():
            if k in 'Token':
                continue
            if isinstance(v, bool):
                base.append([k, str(v).lower()])
            elif isinstance(v, UUID):
                base.append([k, str(v)])
            elif not isinstance(v, list) and not isinstance(v, dict):
                base.append([k, v])

        base.sort(key=lambda i: i[0])
        values = ''.join(map(lambda i: str(i[1]), base))

        m = hashlib.sha256(values.encode())
        
        token = m.hexdigest()
        
        return token

    @staticmethod
    def update_payment_from_response(p: PaymentModel, response: dict) -> PaymentModel:
        for resp_field, model_field in PaymentModel.RESPONSE_FIELDS.items():
            if resp_field in response:
                setattr(p, model_field, response.get(resp_field))

        return p

    def token_correct(self, token: str, data: dict) -> bool:
        return token == self._token(data)

    def init(self, p: PaymentModel) -> PaymentModel:
        urls = {}
        
        if self.success_url:
            urls["SuccessURL"] = self.success_url + f"/{p.pk}"
        
        if self.fail_url:
            urls['FailURL'] = self.fail_url + f"/{p.pk}"
        
        response = self._request('INIT', requests.post, {
            **p.to_json(),
            **urls
        }).json()
        return self.update_payment_from_response(p, response)

    def status(self, p: PaymentModel) -> PaymentModel:
        response = self._request('GET_STATE', requests.post, {'PaymentId': p.payment_id}).json()
        return self.update_payment_from_response(p, response)

    def cancel(self, p: PaymentModel) -> PaymentModel:
        response = self._request('CANCEL', requests.post, {'PaymentId': p.payment_id}).json()
        return self.update_payment_from_response(p, response)

    def get_qr(self, p: PaymentModel) -> str:
        response = self._request('GET_QR', requests.post, {'PaymentId': p.payment_id, 'DataType': 'IMAGE'}).json()
        return response.get("Data", "")

    def spb_pay_test(
        self, p: PaymentModel, is_expired: bool=False, is_rejected: bool=False
    ) -> PaymentModel:
        response = self._request("SPB_PAY_TEST", requests.post, {
            'PaymentId': p.payment_id,
            'IsDeadlineExpired': is_expired,
            'IsRejected': is_rejected
        })
        print(is_expired, is_rejected)
        return self.update_payment_from_response(p, response)
