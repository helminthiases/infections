import collections
import os

import dask
import pandas as pd

import src.data.espen
import src.functions.directories
import src.helminth.consistency


class Points:

    def __init__(self, parameter: collections.namedtuple('Parameter', ['api_key', 'disease', 'level']),
                 fields: list):
        """

        :param parameter:
        :param fields: The list of fields of interest
        """

        self.parameter = parameter
        self.fields = fields

        # The storage area of the countries file
        self.storage = os.path.join(os.getcwd(), 'warehouse', 'data', parameter.level)
        src.functions.directories.Directories().create(self.storage)

        # An ESPEN interface instance
        self.interface = src.data.espen.ESPEN(base='data')

        # Consistency
        self.consistency = src.helminth.consistency.Consistency(level=self.parameter.level)

    @dask.delayed
    def __structure(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        points = data.copy()

        # Ensure that each field's name is lower-cased
        points.rename(mapper=str.lower, axis='columns', inplace=True)

        # Ensure field name consistency
        points.rename(columns={'admin1_code': 'admin1_id', 'admin2_code': 'admin2_id', 'siteid': 'site_id'},
                      inplace=True)

        # Ensure data consistency
        points = self.consistency.exc(data=points.loc[:, self.fields])

        return points

    @dask.delayed
    def __read(self, iso2: str):
        """

        :param iso2:
        :return:
        """

        objects = self.interface.request(
            params={'api_key': self.parameter.api_key, 'disease': self.parameter.disease,
                    'level': self.parameter.level, 'iso2': iso2})
        frame = pd.DataFrame.from_records(objects)

        return frame

    @dask.delayed
    def __write(self, data: pd.DataFrame, name: str):
        """

        :param data:
        :param name:
        :return:
        """

        try:
            data.to_csv(path_or_buf=os.path.join(self.storage, '{}.csv'.format(name)),
                        index=False, header=True, encoding='utf-8')
            return '{}: succeeded'.format(name)
        except OSError as err:
            raise Exception(err.strerror)

    def exc(self, segments: list):
        """

        :param segments:
        :return:
        """

        computations = []
        for iso2 in segments:

            frame = self.__read(iso2=iso2)
            frame = self.__structure(data=frame)
            message = self.__write(data=frame, name=iso2)

            computations.append(message)

        dask.visualize(computations, filename='data', format='pdf')
        messages = dask.compute(computations, scheduler='processes')[0]

        return messages
