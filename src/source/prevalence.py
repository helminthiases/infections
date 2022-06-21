"""
Module: prevalence
"""
import pandas as pd


class Prevalence:
    """
    Prevalence calculator
    """

    def __init__(self):
        """

        """

    @staticmethod
    def individual(positive: pd.Series, examined: pd.Series):
        """

        :param positive:
        :param examined:
        :return:
        """

        return positive/examined

    @staticmethod
    def geohelminth(ascariasis: pd.Series, trichuriasis: pd.Series, hookworm: pd.Series):
        """

        :param ascariasis:
        :param trichuriasis:
        :param hookworm:
        :return:
        """

        factor = 1/1.06
        series = (ascariasis + trichuriasis + hookworm) - ascariasis * (trichuriasis + hookworm) + ascariasis.subtract(
            1) * (trichuriasis * hookworm)

        return factor * series
