"""
Module: adjacent
"""
import glob
import logging
import os
import pathlib
import sys

import dask
import pandas as pd


@dask.delayed
def read(path: str):
    """

    :param path: The file to be read
    :return:
    """

    try:
        return pd.read_csv(filepath_or_buffer=path)
    except OSError as err:
        raise Exception(err.strerror) from err


@dask.delayed
def edges(data: pd.DataFrame, name: str, limit: float):
    """

    :param data: An experiments data set
    :param name: The ISO 3166-1 alpha-2 country code of the experiments data
    :param limit: A pair of points are dissimilar if floor(distance between them) > limit
    :return:
    """

    directory = os.path.join(os.getcwd(), 'warehouse', 'data', 'ESPEN', 'networks', 'edges')

    return src.networks.edges.Edges(directory=directory).exc(data=data, name=name, limit=limit)


@dask.delayed
def graphs(data, name: str):
    """

    :param data: The data set, with distance related features, that will be saved.
    :param name: The ISO 3166-1 alpha-2 country code of the experiments data
    :return:
    """

    directory = os.path.join(os.getcwd(), 'warehouse', 'data', 'ESPEN', 'networks', 'graphs')

    return src.networks.graphs.Graphs(directory=directory).exc(data=data, name=name)


def main():
    """
    Determines the closest observation, if any, within a limit of an observation.

    :return:
    """

    # The edges data sets depend on the ESPEN/experiments/reduced/*.csv data sets.
    # The graphs depend on the edges.
    paths = glob.glob(
        pathname=os.path.join(os.getcwd(), 'warehouse', 'data', 'ESPEN', 'experiments', 'reduced', '*.csv'))

    computations = []
    for path in paths:

        name = pathlib.Path(path).stem
        frame = read(path=path)
        frame = edges(data=frame, name=name, limit=config.Config().limit())
        message = graphs(data=frame, name=name)
        computations.append(message)

    dask.visualize(computations, filename='data', format='pdf')
    messages = dask.compute(computations, scheduler='processes')[0]
    logger.info(messages)


if __name__ == '__main__':
    """
    Initial settings
    """

    # paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs).03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # custom classes
    import config
    import src.functions.directories
    import src.networks.edges
    import src.networks.graphs

    # instances
    directories = src.functions.directories.Directories()
    storage = os.path.join(os.getcwd(), 'warehouse', 'data', 'ESPEN', 'networks')
    directories.cleanup(path=os.path.join(storage, 'edges'))
    directories.cleanup(path=os.path.join(storage, 'graphs'))

    main()
