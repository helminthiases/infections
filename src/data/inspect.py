"""
Module: consistency
"""
import pandas as pd


class Inspect:
    """
    Ensures the consistency of a field's data; for the ESPEN data repository

    """

    def __init__(self, level: str):
        """

        :param level: The ESPEN project data levels, e.g., sitelevel (site level), iu (implementation unit)
        """

        self.level = level

    @staticmethod
    def __site(data: pd.DataFrame):
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

        return {
            'sitelevel': self.__site(data=data)
        }.get(self.level, LookupError('{} could not be mapped to a function'.format(self.level)))