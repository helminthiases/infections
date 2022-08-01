"""
Module: prevalence
"""
import numpy as np
import pandas as pd


class Prevalence:
    """
    Prevalence calculator
    """

    def __init__(self):
        """

        """

    @staticmethod
    def single(positive: pd.Series, examined: pd.Series) -> np.ndarray:
        """

        :param positive: positive cases amongst examinations
        :param examined: the number of examinations conducted
        :return:
        """

        return np.where((positive <= examined) & (examined != 0), positive/examined, np.nan)

    @staticmethod
    def geohelminth(ascariasis: np.ndarray, trichuriasis: np.ndarray, hookworm: np.ndarray) -> np.ndarray:
        """
        Calculates the prevalence of any soil transmitted helminth infection via the prevalence values
        of ascariasis, trichuriasis, and hookworm disease

        :param ascariasis: ascariasis prevalence
        :param trichuriasis: trichuriasis prevalence
        :param hookworm: hookworm prevalence
        :return:
        """

        sums = (ascariasis + trichuriasis + hookworm)
        factor = 1 / 1.06
        series = sums - ascariasis * (trichuriasis + hookworm) + (ascariasis - 1) * (trichuriasis * hookworm)

        return factor * series

    def exc(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data: An experiments data set
        :return:
        """

        frame = data.copy()

        ascariasis = self.single(data['asc_positive'], data['asc_examined'])
        trichuriasis = self.single(data['tt_positive'], data['tt_examined'])
        hookworm = self.single(data['hk_positive'], data['hk_examined'])
        helminth = np.where(~np.isnan(ascariasis) & ~np.isnan(trichuriasis) & ~np.isnan(hookworm),
                            self.geohelminth(ascariasis=ascariasis, trichuriasis=trichuriasis, hookworm=hookworm),
                            np.nan)

        frame.loc[:, 'hk_prevalence'] = hookworm
        frame.loc[:, 'asc_prevalence'] = ascariasis
        frame.loc[:, 'tt_prevalence'] = trichuriasis
        frame.loc[:, 'sth_prevalence'] = helminth

        return frame
