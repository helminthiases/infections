import numpy as np
import pandas as pd


class Measures:

    def __init__(self):
        """

        """

    @staticmethod
    def __frequencies(ascariasis: pd.Series, trichuriasis: pd.Series, hookworm: pd.Series):
        """
        the number of examinations per disease must be equivalent

        :param ascariasis:
        :param trichuriasis:
        :param hookworm:
        :return:
        """

        condition = (ascariasis == trichuriasis) == (ascariasis == hookworm)

        return condition

    @staticmethod
    def __fractions(cases: pd.Series, examinations: pd.Series):
        """
        The number of cases must not exceed the number of examinations conducted

        :param cases:
        :param examinations:
        :return:
        """

        condition = (cases <= examinations)

        return condition

    def exc(self, data: pd.DataFrame):
        """

        :param data:  An experiments data set
        :return:
        """

        frequencies = self.__frequencies(ascariasis=data['asc_examined'],
                                         trichuriasis=data['tt_examined'],
                                         hookworm=data['hk_examined'])

        fractions = np.empty(shape=[data.shape[0], 1])
        for c, e in zip(['asc_positive', 'tt_positive', 'hk_positive'], ['asc_examined', 'tt_examined', 'hk_examined']):

            fractions = np.concatenate((fractions,
                                        self.__fractions(cases=data[c], examinations=data[e])))
