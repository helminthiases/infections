import src.data.espen

import pandas as pd


class Units:

    def __init__(self, key: str):
        """

        :param key:
        """

        self.key = key
        self.fields = ['admin0_id', 'admin1', 'admin1_id', 'admin2', 'admin2_id', 'iu_name', 'iu_id', 'iu_code']

    def __structure(self, data: pd.DataFrame):

        units = data.copy().loc[:, self.fields].drop_duplicates()
        conditions = units.loc[:, ['admin1_id', 'admin2_id', 'iu_id']].isna().any(axis='columns')
        print(conditions)

        return units.loc[~conditions, :]

    def exc(self):
        """

        :return:
        """

        objects = src.data.espen.ESPEN(base='cartographies').request(
            params={'api_key': self.key})

        frame = pd.DataFrame.from_records(objects)
        frame = self.__structure(data=frame)

        return frame
