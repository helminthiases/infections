"""
Module: graphs
"""
import os

import networkx as nx
import numpy as np
import pandas as pd

import src.functions.directories
import src.functions.streams


class Graphs:
    """
    Graphs of geographic coordinates
    """

    def __init__(self, directory: str):
        """

        """

        # storage
        self.directory = directory

    @staticmethod
    def __identifiers(components: list) -> pd.DataFrame:
        """

        :param components: sets of connected edges
        :return:
        """

        frame = pd.DataFrame(data={'component': components})
        frame.loc[:, 'identifier'] = np.linspace(start=1, stop=frame.shape[0], num=frame.shape[0], endpoint=True,
                                                 dtype=np.int64)
        frame = frame.explode(column='component', ignore_index=True)
        frame.loc[:, 'component'] = frame['component'].astype(np.int64, errors='raise').values
        frame.rename(columns={'component': 'id'}, inplace=True)

        return frame

    def __write(self, data: pd.DataFrame, name: str) -> str:
        """

        :param data: The data set, with distance related features, that will be saved.
        :param name: The stem name.
        :return:
        """

        path = os.path.join(self.directory, f'{name}.csv')

        return src.functions.streams.Streams().write(data=data, path=path)

    def partial(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data:
        :return:
        """

        # sets of connected edges, i.e., components
        connections = nx.from_pandas_edgelist(data, source='src', target='dst')
        components = list(nx.connected_components(connections))

        # hence, the new identification codes
        frame = self.__identifiers(components=components)
        frame = data.copy().merge(frame.copy(), on='id', how='left')

        return frame

    def exc(self, data: pd.DataFrame, name: str) -> str:
        """

        :param data: An experiments data set
        :param name: The ISO 3166-1 alpha-2 country code of the experiments data
        :return:
        """

        # calculations
        frame = self.partial(data=data)

        # preserve
        message = self.__write(data=frame, name=name)

        return message
