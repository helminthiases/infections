import pandas as pd


class Sites:

    def __init__(self):
        """

        """

        self.fields = ['iso2', 'iso3', 'admin1_id', 'admin2_id', 'iu_id', 'location', 'site_id',
                       'longitude', 'latitude', 'location_type']

    def __structure(self, data: pd.DataFrame):

        sites = data.copy().loc[:, self.fields].drop_duplicates()
        print(sites.info())

    def exc(self, frame: pd.DataFrame):
        """

        :return:
        """

        self.__structure(data=frame)
