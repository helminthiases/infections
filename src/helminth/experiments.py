"""
Module: examinations
"""
import logging
import os
import sys
import glob
import dask

import pandas as pd


class Experiments:

    def __init__(self):
        """

        """

        self.paths = glob.glob(os.path.join(os.getcwd(), 'data', 'ESPEN', 'experiments'))

    @dask.delayed
    def __read(self, uri: str):
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

    

    def exc(self):
        """

        :return:
        """

        for path in self.paths:

            self.__read(uri=path)



