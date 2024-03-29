"""
Module: distances
"""
import os

import geopandas as gpd
import numpy as np
import pandas as pd

import src.functions.directories
import src.functions.streams


class Edges:
    """
    Nearest point calculations
    """

    def __init__(self, directory: str):
        """

        """

        # directory
        self.directory = directory

    @staticmethod
    def __distances(data: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """

        :param data:
        :return:
        """

        # distances: a square matrix
        distances = data.geometry.apply(lambda x: data.distance(x)).values

        # disable the diagonal
        points = np.diag_indices_from(distances)
        distances[points] = np.nan

        # hence, determine the closest observation to each observation
        frame = data.copy()
        frame.loc[:, 'shortest'] = np.nanmin(a=distances, axis=1)
        frame.loc[:, 'id'] = np.arange(frame.shape[0])
        frame.loc[:, 'src'] = frame['id'].values
        frame.loc[:, 'dst'] = np.nanargmin(a=distances, axis=1)

        return frame

    @staticmethod
    def __dissimilar(data: gpd.GeoDataFrame, limit: float) -> gpd.GeoDataFrame:
        """

        :param data:
        :return:
        """

        frame = data.copy()

        condition = (frame['shortest'] // 1).astype(int) > limit
        frame.loc[condition, 'dst'] = frame.loc[condition, 'src']

        return frame

    def __write(self, data: pd.DataFrame, name: str) -> str:
        """

        :param data: The data set, with distance related features, that will be saved.
        :param name: The stem name.
        :return:
        """

        path = os.path.join(self.directory, f'{name}.csv')

        return src.functions.streams.Streams().write(data=data, path=path)

    def partial(self, data: pd.DataFrame, limit: float) -> pd.DataFrame:

        # converting the data frame to a geographic data frame
        frame = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(x=data.longitude, y=data.latitude))
        frame.set_crs(crs='EPSG:4326', inplace=True)
        frame.to_crs(crs='EPSG:3857', inplace=True)

        # distance
        frame = self.__distances(data=frame)
        frame = self.__dissimilar(data=frame, limit=limit)

        # preserve
        frame.drop(columns=['geometry'], inplace=True)

        return frame

    def exc(self, data: pd.DataFrame, name: str, limit: float) -> pd.DataFrame:
        """

        :param data: An experiments data set
        :param name: The ISO 3166-1 alpha-2 country code of the experiments data
        :param limit: A pair of points are dissimilar if floor(the distance between them) > limit
        :return:
        """

        # calculations
        frame = self.partial(data=data, limit=limit)

        # preserve
        self.__write(data=frame, name=name)

        return frame
