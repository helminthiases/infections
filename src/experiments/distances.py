import pandas as pd
import numpy as np

import geopandas as gpd


class Distances:

    def __init__(self):
        """

        """

    @staticmethod
    def __distances(data: gpd.GeoDataFrame):
        """

        :param data:
        :return:
        """

        # distances: a square matrix
        distances = data.geometry.apply(lambda x: data.distance(x)).values

        # disable the diagonal
        np.fill_diagonal(distances, np.nan)

        # hence, determine the closest observation to each observation
        frame = data.copy()
        frame.loc[:, 'shortest'] = np.nanmin(a=distances, axis=1)
        frame.loc[:, 'id'] = frame.copy().index.values
        frame.loc[:, 'src'] = frame['id'].values
        frame.loc[:, 'dst'] = np.nanargmin(a=distances, axis=1)

        return frame

    @staticmethod
    def __dissimilar(data: gpd.GeoDataFrame, limit: float):
        """

        :param data:
        :return:
        """

        frame = data.copy()
        condition = (frame['shortest'].floordiv(1) > limit)
        frame.loc[condition, 'dst'] = frame.loc[condition, 'src']

        return frame

    def exc(self, data: pd.DataFrame, limit: float):
        """

        :param data: An experiments data set
        :param limit: A pair of points are dissimilar if the distance between them is > limit
        :return:
        """

        # converting the data frame to a geographic data frame
        frame = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(x=data.longitude, y=data.latitude))
        frame.set_crs(crs='EPSG:4326', inplace=True)
        frame.to_crs(crs='EPSG:3857', inplace=True)

        # distance
        frame = self.__distances(data=frame)
        frame = self.__dissimilar(data=frame, limit=limit)

        return frame
