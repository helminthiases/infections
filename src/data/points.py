import src.data.espen

import pandas as pd


class Points:

    def __init__(self, key: str):
        """

        :param key:
        """

        self.key = key
        self.fields = ['iso2', 'iso3', 'admin0_id', 'admin1_id', 'admin2_id', 'iu_id', 'iu_code']

    @staticmethod
    def __structure(data: pd.DataFrame):

        points = data.copy()
        points.rename(mapper=str.lower, axis='columns', inplace=True)
        points.rename(columns={'admin1_code': 'admin1_id', 'admin2_code': 'admin2_id', 'siteid': 'site_id'}, inplace=True)

        print(data.head())
        print(data.info())

    def exc(self, level: str, iso2_strings: list):
        """

        :return:
        """

        interface = src.data.espen.ESPEN(base='data')

        for iso2 in iso2_strings:

            objects = interface.request(params={'api_key': self.key, 'disease': 'sth', 'level': level, 'iso2': iso2})
            frame = pd.DataFrame.from_records(objects)
            self.__structure(data=frame)
