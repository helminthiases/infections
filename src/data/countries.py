import src.data.espen
import pandas as pd


class Countries:

    def __init__(self, key: str):
        """

        :param key: API Key
        """

        self.key = key

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        objects = src.data.espen.ESPEN(base='cartographies').request(
            params={'api_key': self.key, 'admin_level': 'admin0'})

        frame = pd.DataFrame.from_records(objects)

        return frame

