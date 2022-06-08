import requests


class ESPEN:

    def __init__(self, fields):

        # The API end point
        self.endpoint = 'https://admin.espen.afro.who.int/'

        # API fields of interest
        self.fields = fields

    def __request(self, url: str):

        try:
            response = requests.get(url=url, timeout=18)
            response.raise_for_status()
        except requests.RequestException as err:
            raise Exception(err)

        if response.status_code != 200:
            return None
        else:
            return response.json()

    def exc(self, interests: list):
        """
        In progress

        :return:
        """

        for interest in interests:

            objects = self.__request(url=interest)
            print(objects)
