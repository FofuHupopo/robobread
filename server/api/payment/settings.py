from django.conf import settings
from functools import lru_cache


DEFAULT_CONFIG = {
    'URLS': {
        'INIT': 'https://securepay.tinkoff.ru/v2/Init',
        'GET_STATE': 'https://securepay.tinkoff.ru/v2/GetState',
        'CANCEL': 'https://securepay.tinkoff.ru/v2/Cancel',
        'GET_QR': 'https://securepay.tinkoff.ru/v2/GetQr'
    },
    'TAXATION': 'usn_income',
    'ITEM_TAX': 'none',
    'TERMINAL_KEY': '',
    'SECRET_KEY': '',
    'SUCCESS_URL': '',
    'FAIL_URL': '',
    'RECEIPT_EMAIL': '',
    'RECEIPT_PHONE': ''
}


@lru_cache()
def get_config() -> dict:
    user_config = getattr(settings, 'TINKOFF_PAYMENTS_CONFIG', {})

    config = DEFAULT_CONFIG.copy()
    config.update(user_config)

    return config


@lru_cache
def get_config_value(key, default=None):
    return get_config().get(key, default)
