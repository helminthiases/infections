
class Units:

    def __init__(self, key: str):
        """

        :param key:
        """

        self.key = key
        self.fields = {'ADMIN0': 'admin0', 'ADMIN1': 'admin1', 'ADMIN1D': 'admin1_id', 'ADMIN2': 'admin2_id',
                       'IUs_ADM': 'iu_adm', 'IUs_NAME': 'iu_name', 'IU_ID': 'iu_id', 'IU_CODE': 'iu_code'}

    def exc(self):
        """

        :return:
        """