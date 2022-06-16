import logging
import os

import pandas as pd

import src.helminth.espen
import src.functions.directories


class Countries:

    def __init__(self, key: str):
        """

        :param key: API Key
        """

        # API Key
        self.key = key

        # The storage area of the countries file
        self.storage = os.path.join(os.getcwd(), 'warehouse', 'gazetteer')
        src.functions.directories.Directories().create(self.storage)

        # The required fields, and the grouping fields for determining distinct
        # data years per country
        self.fields = ['year', 'continent', 'region', 'who_region', 'admin0', 'admin0_id',
                       'iso2', 'iso3', 'admin_level']
        self.group = ['iso2', 'iso3', 'admin_level', 'admin0', 'admin0_id', 'region',
                      'who_region', 'continent']

    def __structure(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data:
        :return:
        """

        frame = data.copy().loc[:, self.fields].drop_duplicates()
        countries = frame.groupby(self.group)[['year']].agg(lambda x: ', '.join(x.astype(str)))
        countries.reset_index(drop=False, inplace=True)

        return countries

    def __write(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        try:
            data.to_csv(path_or_buf=os.path.join(self.storage, 'countries.csv'),
                        index=False, header=True, encoding='utf-8')
            return True
        except OSError as err:
            raise Exception(err.strerror)

    def exc(self):
        """

        :return:
        """

        objects = src.helminth.espen.ESPEN(base='cartographies').request(
            params={'api_key': self.key, 'admin_level': 'admin0'})
        frame = pd.DataFrame.from_records(objects)
        frame = self.__structure(data=frame)

        if self.__write(data=frame):
            logging.basicConfig(level=logging.INFO,
                                format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                                datefmt='%Y-%m-%d %H:%M:%S')
            logger = logging.getLogger(__name__)
            logger.info('The countries gazetteer is available in {}'.format(self.storage.replace(os.getcwd(), '')))
