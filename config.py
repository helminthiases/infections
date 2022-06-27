import collections


class Config:

    def __init__(self):
        """

        """

    @staticmethod
    def fields():
        experiments = ['iso3', 'iso2', 'admin1_id', 'admin2_id', 'iu_id',
                       'location', 'site_id', 'longitude', 'latitude', 'georeliability', 'location_type',
                       'survey_type', 'year', 'age_start', 'age_end',
                       'hk_examined', 'hk_positive', 'hk_perc_highinfection', 'hk_perc_moderateinfection',
                       'asc_examined', 'asc_positive', 'asc_perc_highinfection', 'asc_perc_moderateinfection',
                       'tt_examined', 'tt_positive', 'tt_perc_highinfection', 'tt_perc_moderateinfection',
                       'quality', 'sn']

        countries = ['iso2', 'iso3', 'admin_level', 'admin0', 'admin0_id', 'region', 'who_region', 'continent']

        Fields = collections.namedtuple(typename='Fields', field_names=['experiments', 'countries'])

        return Fields._make((experiments, countries))
