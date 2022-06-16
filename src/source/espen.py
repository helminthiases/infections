import requests


class ESPEN:

    def __init__(self, base: str):

        # The API end point
        self.endpoint = 'https://admin.espen.afro.who.int/api/{base}'.format(base=base)

    def request(self, params: dict) -> list:

        try:
            response = requests.get(url=self.endpoint, params=params, timeout=33)
            response.raise_for_status()
        except requests.RequestException as err:
            raise Exception(err)

        if response.status_code != 200:
            return list()
        else:
            return response.json()
