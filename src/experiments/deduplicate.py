"""
Module: deduplicate
"""
import os
import pandas as pd
import collections

import config

import src.networks.edges
import src.networks.graphs
import src.functions.directories


class Deduplicate:
    """
    Excludes sites that have more than one record during the same year
    """

    def __init__(self, path: str):
        """

        :param path: directory
        """

        # Equivalence Limits
        self.limit = config.Config().limit()

        # paths, unused
        Paths = collections.namedtuple(typename='Paths', field_names=['edges', 'graphs'])
        paths = Paths._make((os.path.join(path, 'edges'), os.path.join(path, 'graphs')))

        # instances
        self.edges = src.networks.edges.Edges(directory=paths.edges)
        self.graphs = src.networks.graphs.Graphs(directory=paths.graphs)

    @staticmethod
    def __deduplicate(data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data:
        :return:
        """

        # frequencies of year & identifier pairings
        frequencies = data[['year', 'identifier']].groupby(by=['year', 'identifier']).value_counts()
        frequencies.name = 'N'
        frequencies = frequencies.copy().to_frame()
        frequencies.reset_index(drop=False, inplace=True)

        # observations to exclude
        exclude = frequencies.loc[frequencies['N'] > 1, 'identifier'].values

        # excluding
        frame = data.copy().loc[~data['identifier'].isin(exclude), :]

        return frame

    def exc(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data:
        :return:
        """

        frame = self.edges.partial(data=data, limit=self.limit)
        frame = self.graphs.partial(data=frame)
        frame = self.__deduplicate(data=frame)

        return frame
