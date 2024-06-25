import types
import requests
import json


class ModBusHTTPException(Exception):
    pass


class ModBusCommand:
    def _request(self, url: str, method: types.FunctionType, data: dict) -> requests.Response:
        r = method(f"http://127.0.0.1:8001/api/interaction/{url}", data=json.dumps(data), headers={'Content-Type': 'application/json'})

        if r.status_code != 200:
            raise ModBusHTTPException('bad status code')

        return r
        
    def sell_item(self, cell_number):
        self._request(f"sell/{cell_number}", requests.get, {})
        print(f"selled item in cell {cell_number}")
