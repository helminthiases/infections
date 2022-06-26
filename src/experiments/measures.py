"""
Module: measures
"""
import pandas as pd


class Measures:
    """
    Drops the records wherein all the disease measures do not exist
    """

    def __init__(self):
        """

        """

        self.fields = ['asc_positive', 'tt_positive', 'hk_positive', 'asc_examined', 'tt_examined', 'hk_examined']

    def exc(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        condition = data[self.fields].notna().all(axis=1)
        frame = data.copy().loc[condition, :]

        return frame
