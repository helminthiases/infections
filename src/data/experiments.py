"""
Module: experiments
"""
import glob
import os
import pathlib

import dask
import pandas as pd

import src.experiments.format
import src.experiments.time
import src.experiments.geographical
import src.experiments.measures

import src.functions.directories
import src.functions.streams


class Experiments:
    """
    Prepares, inspects, the raw experiments data.
    """

    def __init__(self):
        """

        """

        # Reading and writing
        self.streams = src.functions.streams.Streams()

        # The storage area of the countries file
        self.storage = os.path.join(os.getcwd(), 'warehouse', 'data', 'ESPEN', 'experiments')
        for directory in ['formatted', 'reduced', 'equivalent']:
            src.functions.directories.Directories().create(os.path.join(self.storage, directory))

    @dask.delayed
    def __read(self, uri: str):
        """
        Reads ESPEN STH experiments data

        :param uri: The local path + file name string
        :return:
        """

        return self.streams.read(uri=uri)

    @dask.delayed
    def __format(self, data: pd.DataFrame, name: str):
        """

        :param data:
        :param name:
        :return:
        """

        if data.empty:
            return data

        frame = src.experiments.format.Format().exc(data=data)

        self.streams.write(data=frame, path=os.path.join(self.storage, 'formatted', f'{name}.csv'))

        return frame

    @dask.delayed
    def __reduce(self, data: pd.DataFrame, name: str):
        """

        :param data:
        :param name:
        :return:
        """

        frame = src.experiments.time.Time().exc(data=data)
        frame = src.experiments.geographical.Geographical().exc(data=frame)
        frame = src.experiments.measures.Measures().exc(data=frame)

        self.streams.write(data=frame, path=os.path.join(self.storage, 'reduced', f'{name}.csv'))

        return frame

    @staticmethod
    @dask.delayed
    def __equivalent(data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        frame = data.copy()
        state = frame.empty

        return f'in progress {state}'

    def exc(self):
        """

        :return:
        """

        paths = glob.glob(os.path.join(os.getcwd(), 'data', 'ESPEN', 'experiments', '*.json'))

        computations = []
        for path in paths:

            name = pathlib.Path(path).stem

            frame = self.__read(uri=path)
            frame = self.__format(data=frame, name=name)
            frame = self.__reduce(data=frame, name=name)
            message = self.__equivalent(data=frame)

            computations.append(message)

        dask.visualize(computations, filename='data', format='pdf')
        messages = dask.compute(computations, scheduler='processes')[0]

        return messages
