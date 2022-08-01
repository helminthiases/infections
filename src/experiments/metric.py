"""
Modules: metric
"""
import pandas as pd

import src.experiments.plausible
import src.experiments.equivalent


class Metric:
    """
    About the prevalence metric
    """

    def __init__(self):
        """

        """

    @staticmethod
    def plausible(data: pd.DataFrame) -> pd.DataFrame:
        """
        If a geohelminth prevalence value depends on existing examinations & positive tests values w.r.t.
        ALL three helminth disease types then a plausible observation is one that abides by such a norm.

        :param data:
        :return:
        """

        return src.experiments.plausible.Plausible().exc(data=data)

    @staticmethod
    def equivalent(data: pd.DataFrame) -> pd.DataFrame:
        """
        At each location it's quite probable that the same set of people undergo ascariasis, trichuriasis, and
        hookworm examinations.  Hence, the diseases should have equivalent examinations numbers.

        :param data:
        :return:
        """

        return src.experiments.equivalent.Equivalent().exc(data=data)
