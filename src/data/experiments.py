"""
Module: experiments
"""
import glob
import os
import pathlib

import dask
import pandas as pd

import src.experiments.equivalent
import src.experiments.baseline
import src.experiments.geographical
import src.experiments.measures
import src.experiments.time
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
        src.functions.directories.Directories().cleanup(self.storage)
        for directory in ['baseline', 'reduced', 'equivalent']:
            src.functions.directories.Directories().create(os.path.join(self.storage, directory))

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
    def __baseline(self, data: pd.DataFrame, name: str):
        """

        :param data:
        :param name:
        :return:
        """

        if data.empty:
            return data

        frame = src.experiments.baseline.Baseline().exc(data=data)

        self.streams.write(data=frame, path=os.path.join(self.storage, 'baseline', f'{name}.csv'))

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

    @dask.delayed
    def __equivalent(self, data: pd.DataFrame, name: str):
        """

        :param data:
        :param name:
        :return:
        """

        frame = src.experiments.equivalent.Equivalent().exc(data=data)

        message = self.streams.write(data=frame, path=os.path.join(self.storage, 'equivalent', f'{name}.csv'))

        return message

    def exc(self):
        """

        :return:
        """

        paths = glob.glob(os.path.join(os.getcwd(), 'data', 'ESPEN', 'experiments', '*.json'))

        computations = []
        for path in paths:
            name = pathlib.Path(path).stem

            frame = self.__read(uri=path)
            frame = self.__baseline(data=frame, name=name)
            frame = self.__reduce(data=frame, name=name)
            message = self.__equivalent(data=frame, name=name)

            computations.append(message)

        dask.visualize(computations, filename='data', format='pdf')
        messages = dask.compute(computations, scheduler='processes')[0]

        return messages
