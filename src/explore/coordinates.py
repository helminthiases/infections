import glob
import logging
import os
import pathlib

import geopandas as gpd
import numpy as np
import pandas as pd


def main():

    # The storage area of the site level data
    path = os.path.join(os.getcwd(), 'warehouse', 'data', 'ESPEN', 'experiments')

    # The list of files therein
    items = glob.glob(pathname=os.path.join(path, '*.csv'))

    # Exploring coordinate settings
    for item in items[1:2]:

        logger.info(pathlib.Path(item).stem)

        observations = pd.read_csv(filepath_or_buffer=item, header=0, encoding='utf-8')
        observations = observations.copy().loc[observations['georeliability'] != 99, :]

        frame = gpd.GeoDataFrame(observations,
                                 geometry=gpd.points_from_xy(x=observations.longitude, y=observations.latitude))
        frame.set_crs(crs='EPSG:4326', inplace=True)
        frame.to_crs(crs='EPSG:3857', inplace=True)

        # distances
        sample = frame.geometry.apply(lambda x: frame.distance(x)).values
        sample = np.triu(m=sample, k=1)

        # reference
        reference = np.nan*np.ones_like(a=sample)
        reference = np.tril(m=reference, k=0)

        # distances within upper triangular area only
        values: np.ndarray = reference + sample
        index = values.shape[0] - 1
        values[index, :] = values[:, index]

        L = np.all(np.isnan(values), axis=1)
        logger.info(L)

        beta = np.nanargmin(a=values, axis=1)
        logger.info(beta)

        sigma = np.nanmin(a=values, axis=1)
        logger.info(sigma)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    main()
