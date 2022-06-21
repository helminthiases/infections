"""
Module: points
"""
import os

import dask
import pandas as pd

import src.source.espen
import src.functions.directories
import src.source.consistency


class Points:
    """
    Reads data from the ESPEN data repository
    """

    def __init__(self, level: str, fields: list):
        """

        :param level: WHO experiment level - site or implementation unit
        :param fields: The list of fields of interest
        """

        self.fields = fields

        # The storage area of the countries file
        self.storage = os.path.join(os.getcwd(), 'warehouse', 'data', level)
        src.functions.directories.Directories().create(self.storage)

        # An ESPEN interface instance
        self.interface = src.source.espen.ESPEN(base='data')

        # Consistency
        self.consistency = src.source.consistency.Consistency(level=level)

    @dask.delayed
    def __structure(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        points = data.copy()

        if points.empty:
            return points
        else:
            # Ensure that each field's name is lower-cased
            # Ensure field name consistency
            # Ensure data consistency
            points.rename(mapper=str.lower, axis='columns', inplace=True)
            points.rename(columns={'admin1_code': 'admin1_id', 'admin2_code': 'admin2_id', 'siteid': 'site_id'},
                          inplace=True)
            points = self.consistency.exc(data=points.loc[:, self.fields])
            return points

    @dask.delayed
    def __read(self, params: dict):
        """

        :param params:
        :return:
        """

        objects = self.interface.request(params=params)

        if len(objects) == 0:
            frame = pd.DataFrame()
        else:
            frame = pd.DataFrame.from_records(objects)

        return frame

    @dask.delayed
    def __write(self, data: pd.DataFrame, name: str):
        """

        :param data:
        :param name:
        :return:
        """

        if data.empty:
            return '{}: empty'.format(name)
        else:
            try:
                data.to_csv(path_or_buf=os.path.join(self.storage, '{}.csv'.format(name)),
                            index=False, header=True, encoding='utf-8')
                return '{}: succeeded'.format(name)
            except OSError as err:
                raise Exception(err.strerror)

    def exc(self, parameters: list):
        """

        :param parameters:
        :return:
        """

        computations = []
        for params in parameters:

            frame = self.__read(params=params)
            frame = self.__structure(data=frame)
            message = self.__write(data=frame, name=params['iso2'])

            computations.append(message)

        dask.visualize(computations, filename='data', format='pdf')
        messages = dask.compute(computations, scheduler='processes')[0]

        return messages
