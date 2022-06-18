import glob
import os
import dask

import pandas as pd

import src.functions.directories


class Identifiers:

    def __init__(self):
        """

        """

        # Data Source
        source = os.path.join(os.getcwd(), 'warehouse', 'data', 'sitelevel')
        self.items = glob.glob(pathname=os.path.join(source, '*.csv'))

        # Storage
        self.storage = os.path.join(os.getcwd(), 'warehouse', 'explore')
        src.functions.directories.Directories().create(path=self.storage)

    @dask.delayed
    def __read(self, item: str) -> pd.DataFrame:

        observations = pd.read_csv(filepath_or_buffer=item, header=0, encoding='utf-8',
                                   usecols=['iso3', 'iso2', 'site_id'])
        available = sum(observations['site_id'].notna())
        fraction = available / observations.shape[0]

        frame = observations[['iso3', 'iso2']].drop_duplicates()
        frame.loc[:, 'available'] = available
        frame.loc[:, 'observations'] = observations.shape[0]
        frame.loc[:, 'fraction'] = fraction

        return frame

    def __write(self, data: pd.DataFrame) -> str:

        name = os.path.join(self.storage, 'identifiers.csv')

        try:
            data.to_csv(path_or_buf=name, index=False, header=True, encoding='utf-8')
            return 'A summary of the availability of site identifiers: {}'.format(name.replace(os.getcwd(), ''))
        except OSError as err:
            raise Exception(err.strerror)

    def exc(self) -> str:

        computations = []
        for item in self.items:

            frame = self.__read(item=item)
            computations.append(frame)

        dask.visualize(computations, filename='data', format='pdf')
        calculations = dask.compute(computations, scheduler='processes')[0]
        calculations = pd.concat(calculations, axis=0, ignore_index=True)

        return self.__write(data=calculations)
