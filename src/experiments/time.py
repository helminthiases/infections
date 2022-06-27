"""
Module: time
"""
import pandas as pd


class Time:
    """
    Drops the experiment records that do not have their time values
    """

    def __init__(self):
        """

        """

    @staticmethod
    def __year(data: pd.DataFrame):
        """

        :param data: An experiments data frame
        :return:
        """

        frame = data.copy().loc[data['year'].notna(), :]

        return frame

    def exc(self, data: pd.DataFrame):
        """

        :param data: An experiments data frame
        :return:
        """

        frame = self.__year(data=data)

        return frame
