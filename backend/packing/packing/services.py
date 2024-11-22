import requests


class ProductService:
    ENDPOINT = "/api/products"

    def __init__(self, ip_address) -> None:
        self.ip_address = ip_address

    def _request(self, method, url, data={}, query={}) -> requests.Response:
        print(f"http://{self.ip_address}{self.ENDPOINT}/{url}")

        r: requests.Response = method(
            f"http://{self.ip_address}{self.ENDPOINT}/{url}",
            json=data,
            params=query
        )

        if r.status_code not in (200, 201):
            raise ValueError(f"({r.status_code}) {r.text}")

        return r

    def get_products(self):
        return self._request(requests.get, "all-product").json()

    def add_packing(self, data):
        return self._request(requests.post, "packing", data=data).json()


class AccountingService:
    HOST = "127.0.0.1"
    PORT = 8005
    ENDPOINT = "/api"

    @classmethod
    def _request(cls, method, url, data={}, query={}) -> requests.Response:
        r: requests.Response = method(
            f"http://{cls.HOST}:{cls.PORT}{cls.ENDPOINT}/{url}",
            json=data,
            params=query
        )

        if r.status_code not in (200, 201):
            raise ValueError(f"({r.status_code}) {r.text}")

        return r

    @classmethod
    def get_vending_machines(cls):
        return cls._request(requests.get, "vending-machines/sync").json()
    
    @classmethod
    def add_packing(cls, data):
        return cls._request(requests.post, "packing/packing", data=data).json()
