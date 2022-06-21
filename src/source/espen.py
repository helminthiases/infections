"""
Module: espen
"""
import requests


class ESPEN:
    """
    Queries, and extracts from, ESPEN repositories
    """

    def __init__(self, base: str):
        """

        :param base: The ESPEN repository to read from, e.g., data, cartography, etc.
        """

        # The API end point
        self.endpoint = 'https://admin.espen.afro.who.int/api/{base}'.format(base=base)

    def request(self, params: dict) -> list:
        """

        :param params: The ESPEN API parameters for querying an ESPEN repository
        :return:
        """

        try:
            response = requests.get(url=self.endpoint, params=params, timeout=33)
            response.raise_for_status()
        except requests.RequestException as err:
            raise Exception(err)

        if response.status_code != 200:
            return list()
        else:
            return response.json()
