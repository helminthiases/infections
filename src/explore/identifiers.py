import glob
import os
import dask

import pandas as pd


class Identifiers:

    def __init__(self):
        """

        """

        path = os.path.join(os.getcwd(), 'warehouse', 'data', 'sitelevel')
        self.items = glob.glob(pathname=os.path.join(path, '*.csv'))

    @dask.delayed
    def __read(self, item: str):

        observations = pd.read_csv(filepath_or_buffer=item, header=0, encoding='utf-8',
                                   usecols=['iso3', 'iso2', 'site_id'])
        available = sum(observations['site_id'].notna())
        fraction = available / observations.shape[0]

        frame = observations[['iso3', 'iso2']].drop_duplicates()
        frame.loc[:, 'available'] = available
        frame.loc[:, 'fraction'] = fraction

        return frame

    def exc(self):

        computations = []
        for item in self.items:

            frame = self.__read(item=item)
            computations.append(frame)

        dask.visualize(computations, filename='data', format='pdf')
        calculations = dask.compute(computations, scheduler='processes')[0]
        calculations = pd.concat(calculations, axis=0, ignore_index=True)

        return calculations
