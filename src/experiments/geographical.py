"""
Module: geographical
"""
import pandas as pd


class Geographical:
    """
    Determines acceptable observations in relation to geographic variables
    """

    def __init__(self):
        """

        """

    @staticmethod
    def __geo(data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data:
        :return:
        """

        # An ESPEN observation wherein <geo reliability> = 99 has absolutely unreliable geographic values
        frame = data.copy().loc[data['georeliability'] != 99, :]

        return frame

    @staticmethod
    def __administrations(data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        # The cases whereby the codes of both administrative levels - levels 1 & 2 - are present
        condition = data[['admin1_id', 'admin2_id']].notna()
        condition = condition.all(axis=1)
        frame = data.copy().loc[condition, :]

        return frame

    @staticmethod
    def __coordinates(data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        # The cases whereby both the longitude & latitude values exists
        condition = data[['longitude', 'latitude']].notna()
        condition = condition.all(axis=1)
        frame = data.copy().loc[condition, :]

        return frame

    def exc(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        frame = self.__geo(data=data)
        frame = self.__administrations(data=frame)
        frame = self.__coordinates(data=frame)

        return frame
