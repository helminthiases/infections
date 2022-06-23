"""
Module: countries
"""
import os

import pandas as pd

import src.functions.directories


class Countries:
    """
    Creates a countries gazetteer
    """

    def __init__(self):
        """

        """

        self.source = os.path.join(os.getcwd(), 'data', 'ESPEN', 'cartographies')

        # The storage area of the countries file
        self.storage = os.path.join(os.getcwd(), 'warehouse', 'gazetteer')
        src.functions.directories.Directories().create(self.storage)

        # The required fields
        self.fields = ['iso2', 'iso3', 'admin_level', 'admin0', 'admin0_id', 'region', 'who_region', 'continent']

    def __read(self) -> pd.DataFrame:

        try:
            frame = pd.read_json(path_or_buf=os.path.join(self.source, 'countries.json'))
        except OSError as err:
            raise Exception(err.strerror) from err

        return frame

    def __structure(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data:
        :return:
        """

        frame = data.copy().loc[:, self.fields].drop_duplicates()
        frame.reset_index(drop=False, inplace=True)

        return frame

    def __write(self, data: pd.DataFrame) -> str:
        """

        :param data:
        :return:
        """

        try:
            data.to_csv(path_or_buf=os.path.join(self.storage, 'countries.csv'),
                        index=False, header=True, encoding='utf-8')
            return 'The countries gazetteer is available within {}'.format(self.storage.replace(os.getcwd(), ''))
        except OSError as err:
            raise Exception(err.strerror) from err

    def exc(self) -> str:
        """

        :return:
        """

        frame = self.__read()
        frame = self.__structure(data=frame)
        return self.__write(data=frame)
