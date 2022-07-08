"""
Module: measures
"""
import pandas as pd


class Plausible:
    """
    Drops the records wherein all the disease measures do not exist
    """

    def __init__(self):
        """

        """

        self.fields = ['asc_prevalence', 'tt_prevalence', 'hk_prevalence']

    def exc(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        condition = data[self.fields].notna().all(axis=1)
        frame = data.copy().loc[condition, :]
        frame = pd.DataFrame() if frame.shape[0] < 2 else frame

        return frame
