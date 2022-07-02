"""
Module: adjacent
"""
import glob
import logging
import os
import pathlib
import sys

import dask
import geopandas as gpd
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
def linear(data: pd.DataFrame, limit: float):
    """

    :param data: An experiments data set
    :param limit: A pair of points are dissimilar if floor(distance between them) > limit
    :return:
    """

    return src.networks.linear.Linear().exc(data=data, limit=limit)


@dask.delayed
def streams(data, path):
    """

    :param data: The data set, with distance related features, that will be saved.
    :param path: The storage location.
    :return:
    """

    return src.functions.streams.Streams().write(data=data, path=path)


def main():
    """
    Determines the closest observation, if any, within a limit of an observation.

    :return:
    """

    paths = glob.glob(
        pathname=os.path.join(os.getcwd(), 'warehouse', 'data', 'ESPEN', 'experiments', 'equivalent', '*.csv'))

    computations = []
    for path in paths:
        frame: pd.DataFrame = read(path=path)
        frame: gpd.GeoDataFrame = linear(data=frame, limit=0)
        message: str = streams(data=frame, path=os.path.join(storage, pathlib.Path(path).name))
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
    import src.networks.linear
    import src.functions.streams
    import src.functions.directories

    # storage
    storage = os.path.join(root, 'warehouse', 'data', 'ESPEN', 'networks', 'edges')
    directories = src.functions.directories.Directories()
    directories.cleanup(path=pathlib.Path(storage).parent.__str__())
    directories.create(storage)

    main()
