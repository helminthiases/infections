import glob
import logging
import os

import geopandas as gpd
import pandas as pd


def main():

    # The storage area of the site level data
    path = os.path.join(os.getcwd(), 'warehouse', 'data', 'sitelevel')

    # The list of files therein
    items = glob.glob(pathname=os.path.join(path, '*.csv'))

    # Exploring coordinate settings
    for item in items:
        observations = pd.read_csv(filepath_or_buffer=item, header=0, encoding='utf-8')
        frame = gpd.GeoDataFrame(observations,
                                 geometry=gpd.points_from_xy(x=observations.longitude, y=observations.latitude))
        frame.set_crs(crs='EPSG:4326', inplace=True)
        frame.to_crs(crs='EPSG:3857', inplace=True)
        logger.info(frame.crs)
        logger.info(frame.info())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    main()
