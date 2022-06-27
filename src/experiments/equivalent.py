"""
Module: equivalent
"""
import pandas as pd
import numpy as np


class Equivalent:
    """
    Ensures that only records wherein (a) the number of examinations per disease are equivalent, and (b) the number
    of cases of a disease does not exceed the number of examinations of the disease  - are retained.
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

    @staticmethod
    def __fractions(data: pd.DataFrame) -> np.ndarray:
        """
        The number of cases must not exceed the number of examinations conducted

        :param data: An experiments data set
        :return:
        """

        condition = []
        for cases, examinations in zip(['asc_positive', 'tt_positive', 'hk_positive'], 
                                       ['asc_examined', 'tt_examined', 'hk_examined']):
            less = (data[cases] <= data[examinations])
            less = np.array(less, ndmin=2).transpose()
            condition.append(less)
        condition = np.expand_dims(np.concatenate(condition, axis=1).all(axis=1),
                                   axis=1)

        return condition

    def exc(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data:  An experiments data set
        :return:
        """

        frequencies = self.__frequencies(data=data)
        fractions = self.__fractions(data=data)

        accept = (frequencies & fractions)
        frame = data.copy().loc[accept, :]
        frame = pd.DataFrame() if frame.shape[0] < 2 else frame

        return frame
