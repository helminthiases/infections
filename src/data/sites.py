import src.data.espen

import pandas as pd


class Sites:

    def __init__(self, key: str):
        """

        :param key:
        """

        self.key = key
        self.fields = ['iso2', 'iso3', 'admin0_id', 'admin1_id', 'admin2_id', 'iu_id', 'iu_code']

    @staticmethod
    def __structure(data: pd.DataFrame):

        print(data.info())

    def exc(self):
        """

        :return:
        """

        objects = src.data.espen.ESPEN(base='cartographies').request(
            params={'api_key': self.key})

        frame = pd.DataFrame.from_records(objects)
        self.__structure(data=frame)
