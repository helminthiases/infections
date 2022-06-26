"""
Module: inspect
"""
import pandas as pd


class Formats:
    """
    Inspects the data of specific fields; for the ESPEN data repository

    """

    def __init__(self):
        """

        """

    @staticmethod
    def __text(data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        frame = data.copy()

        frame.loc[:, 'iso3'] = frame['iso3'].str.upper()
        frame.loc[:, 'iso2'] = frame['iso2'].str.upper()

        frame.loc[:, 'location'] = frame.location.str.lower().str.replace('_', ' ').str.replace('-', ' ').str.strip()
        frame.loc[:, 'location_type'] = frame['location_type'].str.lower().str.strip()
        frame.loc[:, 'survey_type'] = frame['survey_type'].str.lower().str.strip()

        return frame

    def exc(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        return  self.__text(data=data)
