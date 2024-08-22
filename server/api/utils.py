import types
import requests
import json
import functools

from django.conf import settings


def run_if_allow_interaction(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if settings.ALLOW_INTERACTION:
            result = method(self, *args, **kwargs)
            return result
        
        print("The command has not been sent, check it.env file")

    return wrapper


class InteractionHTTPException(Exception):
    pass


class InteractionCommand:
    def _request(self, url: str, method: types.FunctionType, data: dict) -> requests.Response:
        r = method(f"http://127.0.0.1:8001/api/interaction/{url}", data=json.dumps(data), headers={'Content-Type': 'application/json'})

        if r.status_code != 200:
            raise InteractionHTTPException('bad status code')

        return r
    
    @run_if_allow_interaction
    def sell_item(self, cell_number):
        self._request(f"sell/{cell_number}", requests.get, {})
        print(f"selled item in cell {cell_number}")

    @run_if_allow_interaction
    def open_door(self):
        self._request(f"open-door/", requests.get, {})
        print(f"Door opened.")
