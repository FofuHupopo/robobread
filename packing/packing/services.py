import requests


class ProductService:
    HOST = "127.0.0.1"
    PORT = 8000
    ENDPOINT = "/api/products"

    @classmethod
    def _request(cls, method, url, data={}, query={}) -> requests.Response:
        r = method(
            f"http://{cls.HOST}:{cls.PORT}{cls.ENDPOINT}/{url}",
            data=data,
            params=query
        )

        if r.status_code != 200:
            raise ValueError(f"Bad status code, got {r.status_code}")

        return r

    @classmethod
    def get_products(cls):
        return ProductService._request(requests.get, "all-product").json()
    
    @classmethod
    def patch_product(cls, id, item):
        return ProductService._request(requests.patch, f"product/{id}", data=item).json()

    @classmethod
    def update_cell_count(cls, id, count):
        return ProductService._request(requests.patch, f"cell/{id}", data={"count": count}).json()
