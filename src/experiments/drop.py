"""
Module: intensity
"""
import pandas as pd


class Drop:
    """
    Drops the intensity related fields
    """

    def __init__(self):
        """

        """

        self.fields = ['hk_perc_highinfection', 'hk_perc_moderateinfection',
                       'asc_perc_highinfection', 'asc_perc_moderateinfection',
                       'tt_perc_highinfection', 'tt_perc_moderateinfection']

    def __drop(self, data: pd.DataFrame):
        """

        :param data: An experiments data frame
        :return:
        """

        frame = data.copy().drop(columns=self.fields)

        return frame

    def exc(self, data: pd.DataFrame):
        """

        :param data: An experiments data frame
        :return:
        """

        return self.__drop(data=data)
