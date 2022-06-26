"""
Module: experiments
"""
import glob
import os
import pathlib

import dask
import pandas as pd

import config
import src.functions.directories
import src.experiments.formats


class Experiments:
    """
    Prepares, inspects, the raw experiments data.
    """

    def __init__(self):
        """

        """

        self.paths = glob.glob(os.path.join(os.getcwd(), 'data', 'ESPEN', 'experiments', '*.json'))

        # The experiment fields of interest
        self.fields = config.Config().fields().experiments

        # Data inspection instance
        self.inspect = src.experiments.formats.Inspect(level='sitelevel')

        # The storage area of the countries file
        self.storage = os.path.join(os.getcwd(), 'warehouse', 'data', 'ESPEN', 'experiments')
        src.functions.directories.Directories().create(self.storage)

    @staticmethod
    @dask.delayed
    def __read(uri: str):
        """
        Reads ESPEN STH experiments data

        :param uri: The local path + file name string
        :return:
        """

        try:
            frame = pd.read_json(path_or_buf=uri)
        except OSError as err:
            raise Exception(err.strerror) from err

        return frame

    @dask.delayed
    def __structure(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        points = data.copy()

        if points.empty:
            return points

        # Ensure that each field's name is lower-cased & in-line with naming patterns. Inspect.
        points.rename(mapper=str.lower, axis='columns', inplace=True)
        points.rename(columns={'admin1_code': 'admin1_id', 'admin2_code': 'admin2_id', 'siteid': 'site_id'},
                      inplace=True)
        points = self.inspect.exc(data=points.loc[:, self.fields])

        return points

    @dask.delayed
    def __write(self, data: pd.DataFrame, name: str):
        """

        :param data:
        :param name:
        :return:
        """

        if data.empty:
            return '{}: empty'.format(name)

        try:
            data.to_csv(path_or_buf=os.path.join(self.storage, '{}.csv'.format(name)),
                        index=False, header=True, encoding='utf-8')
            return '{}: succeeded'.format(name)
        except OSError as err:
            raise Exception(err.strerror) from err

    def exc(self):
        """

        :return:
        """

        computations = []
        for path in self.paths:
            frame = self.__read(uri=path)
            frame = self.__structure(data=frame)
            message = self.__write(data=frame, name=pathlib.Path(path).stem)

            computations.append(message)

        dask.visualize(computations, filename='data', format='pdf')
        messages = dask.compute(computations, scheduler='processes')[0]

        return messages
