
class Units:

    def __init__(self, key: str):
        """

        :param key:
        """

        self.key = key
        self.fields = ['year', 'continent', 'region', 'who_region', 'admin0', 'admin0_id',
                       'iso2', 'iso3', 'admin_level']

    def exc(self):
        """

        :return:
        """