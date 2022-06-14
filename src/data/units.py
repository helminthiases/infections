import logging
import os

import pandas as pd

import src.data.espen
import src.functions.directories


class Units:

    def __init__(self, key: str):
        """

        :param key: API Key
        """

        # API Key
        self.key = key

        # The storage area of the countries file
        self.storage = os.path.join(os.getcwd(), 'warehouse', 'gazetteer')
        src.functions.directories.Directories().create(self.storage)

        # The required fields
        self.fields = ['iso2', 'iso3', 'admin0_id', 'admin1', 'admin1_id',
                       'admin2', 'admin2_id', 'iu_name', 'iu_id', 'iu_code']

    def __structure(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        units = data.copy().loc[:, self.fields].drop_duplicates()
        conditions = units.loc[:, ['admin1_id', 'admin2_id', 'iu_id']].isna().any(axis='columns')

        return units.loc[~conditions, :]

    def __write(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        try:
            data.to_csv(path_or_buf=os.path.join(self.storage, 'units.csv'),
                        index=False, header=True, encoding='utf-8')
            return True
        except OSError as err:
            raise Exception(err.strerror)

    def exc(self):
        """

        :return:
        """

        objects = src.data.espen.ESPEN(base='cartographies').request(
            params={'api_key': self.key})
        frame = pd.DataFrame.from_records(objects)
        frame = self.__structure(data=frame)

        if self.__write(data=frame):
            logging.basicConfig(level=logging.INFO,
                                format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                                datefmt='%Y-%m-%d %H:%M:%S')
            logger = logging.getLogger(__name__)
            logger.info('The countries gazetteer is available in {}'.format(self.storage))
