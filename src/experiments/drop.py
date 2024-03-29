"""
Module: intensity
"""
import pandas as pd


class Drop:
    """
    Drops irrelevant fields; irrelevant to the project, or flawed.
    """

    def __init__(self):
        """

        """

        self.fields = ['hk_perc_highinfection', 'hk_perc_moderateinfection',
                       'asc_perc_highinfection', 'asc_perc_moderateinfection',
                       'tt_perc_highinfection', 'tt_perc_moderateinfection', 'location']

    def __drop(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data: An experiments data frame
        :return:
        """

        frame = data.copy().drop(columns=self.fields)

        return frame

    def exc(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data: An experiments data frame
        :return:
        """

        return self.__drop(data=data)
