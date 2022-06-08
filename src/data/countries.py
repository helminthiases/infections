import src.data.espen
import pandas as pd


class Countries:

    def __init__(self, key: str):
        """

        :param key: API Key
        """

        self.key = key
        self.fields = ['year', 'continent', 'region', 'who_region', 'admin0', 'admin0_id',
                       'iso2', 'iso3', 'admin_level']
        self.group = ['iso2', 'iso3', 'admin_level', 'admin0', 'admin0_id', 'region',
                      'who_region', 'continent']

    def __structure(self, data: pd.DataFrame) -> pd.DataFrame:

        frame = data.copy().loc[:, self.fields].drop_duplicates()
        countries = frame.groupby(self.group)[['year']].agg(lambda x: {', '.join(x.astype(str))})
        countries.reset_index(drop=False, inplace=True)

        return countries

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        objects = src.data.espen.ESPEN(base='cartographies').request(
            params={'api_key': self.key, 'admin_level': 'admin0'})

        frame = pd.DataFrame.from_records(objects)
        frame = self.__structure(data=frame)

        return frame

