import pandas as pd
import os


class Keys:

    def __init__(self):

        self.source = os.path.join(os.getcwd(), 'keys', 'api.json')

    def exc(self):

        try:
            readings = pd.read_json(path_or_buf=self.source)
        except OSError as err:
            raise err

        return readings
