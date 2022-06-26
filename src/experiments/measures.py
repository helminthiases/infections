import numpy as np
import pandas as pd


class Measures:

    def __init__(self):
        """

        """

        self.fields = ['asc_positive', 'tt_positive', 'hk_positive', 'asc_examined', 'tt_examined', 'hk_examined']

    def exc(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        condition = data[self.fields].notna()

