"""
Module: equivalent
"""
import numpy as np
import pandas as pd


class Equivalent:
    """
    Ensures that only records wherein the number of examinations per disease are equivalent are retained.
    """

    def __init__(self):
        """

        """

    @staticmethod
    def __frequencies(data: pd.DataFrame) -> np.ndarray:
        """
        The number of examinations per disease must be equivalent

        :param data: An experiments data set
        :return:
        """

        condition = (data['asc_examined'] == data['tt_examined']) & (data['asc_examined'] == data['hk_examined'])
        condition = np.array(condition, ndmin=2).transpose()

        return condition

    def exc(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data:  An experiments data set
        :return:
        """

        if data.empty:
            return data

        else:
            frequencies = self.__frequencies(data=data)
            frame = data.copy().loc[frequencies, :]
            frame = pd.DataFrame() if frame.shape[0] < 2 else frame

            return frame
