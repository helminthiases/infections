"""
Module: baseline
"""
import pandas as pd

import src.experiments.format
import src.experiments.prevalence


class Baseline:
    """
    Returns the baseline experiments data set wherein

        a. field names are lower case and consistent with common names
        b. text field values are lower case & space stripped
        c. the set includes ascariasis, trichuriasis, and hookworm disease prevalence values
        d. the set includes geohelminth prevalence values; for the formula, refer to prevalence.py
    """

    def __init__(self):
        """

        """

        # instances
        self.format = src.experiments.format.Format()
        self.prevalence = src.experiments.prevalence.Prevalence()

    def exc(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data: an experiments data set
        :return:
        """

        frame = data.copy()
        frame = self.format.exc(data=frame)
        frame = self.prevalence.exc(data=frame)

        return frame
