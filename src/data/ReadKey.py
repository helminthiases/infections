import pandas as pd
import os


class ReadKey:

    def __init__(self):

        self.filestr = os.path.join(os.getcwd(), 'keys', 'api.json')

    def exc(self):

        try:
            readings = pd.read_json(path_or_buf=self.filestr)
        except OSError as err:
            raise err
