"""
Module: inspect
"""
import numpy as np
import pandas as pd

import config


class Format:
    """
    Inspects the data of specific fields; for the ESPEN data repository

    """

    def __init__(self):
        """

        """

        # The experiment fields of interest
        self.fields = config.Config().fields().experiments

        # Address the field names discrepancies
        self.rename = {'admin1_code': 'admin1_id', 'admin2_code': 'admin2_id', 'siteid': 'site_id'}

    def __title(self, data: pd.DataFrame):
        """

        :param data: An ESPEN STH experiments data set
        :return:
        """

        frame = data.copy()

        # Ensure that each field's name is lower-cased & in-line with naming patterns. Inspect.
        frame.rename(mapper=str.lower, axis='columns', inplace=True)
        frame.rename(columns=self.rename, inplace=True)
        
        return frame.loc[:, self.fields]

    @staticmethod
    def __year(data: pd.DataFrame) -> pd.DataFrame:
        """
        If the <year> field value is zero, replace zero with NaN

        :param data: An ESPEN STH experiments data set
        :return:
        """

        frame = data.copy()
        condition = frame['year'] == 0
        frame.loc[condition, 'year'] = np.NAN

        return frame

    @staticmethod
    def __text(data: pd.DataFrame):
        """

        :param data: An ESPEN STH experiments data set
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

        :param data: An ESPEN STH experiments data set
        :return:
        """

        frame = self.__title(data=data)
        frame = self.__text(data=frame)
        frame = self.__year(data=frame)

        return frame
