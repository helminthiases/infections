import src.data.espen

import pandas as pd


class Units:

    def __init__(self, key: str):
        """

        :param key:
        """

        self.key = key
        self.fields: dict = {'ADMIN0': 'admin0', 'ADMIN1': 'admin1', 'ADMIN1D': 'admin1_id', 'ADMIN2': 'admin2_id',
                             'IUs_ADM': 'iu_adm', 'IUs_NAME': 'iu_name', 'IU_ID': 'iu_id', 'IU_CODE': 'iu_code'}

    def __structure(self, data: pd.DataFrame):

        units = data.copy().loc[:, list(self.fields.keys())].drop_duplicates()
        units.rename(columns=self.fields, inplace=True)

        return units

    def exc(self):
        """

        :return:
        """

        objects = src.data.espen.ESPEN(base='cartographies').request(
            params={'api_key': self.key})

        frame = pd.DataFrame.from_records(objects)
        frame = self.__structure(data=frame)

        return frame
