"""
Module: streams
"""
import pathlib

import pandas as pd


class Streams:
    """
    For writing and reading data frames
    """

    def __init__(self):
        """

        """

    @staticmethod
    def write(data: pd.DataFrame, path: str):
        """

        :param data:
        :param path:
        :return:
        """

        name = pathlib.Path(path).stem

        if data.empty:
            return f'{name}: empty'

        try:
            data.to_csv(path_or_buf=path, index=False, header=True, encoding='utf-8')
            return f'{name}: succeeded'
        except OSError as err:
            raise Exception(err.strerror) from err
