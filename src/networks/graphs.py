import networkx as nx
import numpy as np
import pandas as pd


class Graphs:

    def __init__(self):
        """

        """

    @staticmethod
    def __identifiers(components: list):
        sample = pd.DataFrame(data={'component': components})
        sample.loc[:, 'identifier'] = np.linspace(start=1, stop=sample.shape[0], num=sample.shape[0], endpoint=True,
                                                  dtype=np.int64)
        sample = sample.explode(column='component', ignore_index=True)
        sample.loc[:, 'component'] = sample['component'].astype(np.int64, errors='raise').values

    def exc(self, data: pd.DataFrame):
        connections = nx.from_pandas_edgelist(data, source='src', target='dst')
        components = list(nx.connected_components(connections))
        self.__identifiers(components=components)
