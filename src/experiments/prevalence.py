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

        :param positive: positive cases amongst examinations
        :param examined: the number of examinations conducted
        :return:
        """

        return positive/examined

    @staticmethod
    def geohelminth(ascariasis: pd.Series, trichuriasis: pd.Series, hookworm: pd.Series):
        """
        Calculates the prevalence of any soil transmitted helminth infection via the prevalence values
        of ascariasis, trichuriasis, and hookworm disease

        :param ascariasis: ascariasis prevalence
        :param trichuriasis: trichuriasis prevalence
        :param hookworm: hookworm prevalence
        :return:
        """

        factor = 1/1.06
        series = (ascariasis + trichuriasis + hookworm) - ascariasis * (trichuriasis + hookworm) + ascariasis.subtract(
            1) * (trichuriasis * hookworm)

        return factor * series
