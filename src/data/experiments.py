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
import src.functions.streams
import src.experiments.format


class Experiments:
    """
    Prepares, inspects, the raw experiments data.
    """

    def __init__(self):
        """

        """

        self.paths = glob.glob(os.path.join(os.getcwd(), 'data', 'ESPEN', 'experiments', '*.json'))

        # Data inspection instance
        self.format = src.experiments.format.Format()

        # Reading and writing
        self.streams = src.functions.streams.Streams()

        # The storage area of the countries file
        self.storage = os.path.join(os.getcwd(), 'warehouse', 'data', 'ESPEN', 'experiments')
        src.functions.directories.Directories().create(self.storage)

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

        # Format
        frame = self.format.exc(data=data)

        # Write
        self.streams.write(data=frame, path=os.path.join(self.storage, f'{name}.csv'))

        return frame

    @dask.delayed
    def __reduce(self, data: pd.DataFrame, name: str):
        """

        :param data:
        :param name:
        :return:
        """

    @dask.delayed
    def __equivalent(self, data: pd.DataFrame, name: str):
        """
        
        :param data: 
        :param name: 
        :return: 
        """
        
    def exc(self):
        """

        :return:
        """

        computations = []
        for path in self.paths:
            frame = self.__read(uri=path)
            frame = self.__format(data=frame)



            message = ''

            computations.append(message)

        dask.visualize(computations, filename='data', format='pdf')
        messages = dask.compute(computations, scheduler='processes')[0]

        return messages
