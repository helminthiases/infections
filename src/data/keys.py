import json

import os


class Keys:

    def __init__(self):
        """
        Constructor

        The api.json file must be located within infections/keys, and the structure is

            {"host name": "key", "host name": "key", ...}

        """

        self.source = os.path.join(os.getcwd(), 'keys', 'api.json')

    def exc(self, host):
        """

        :param host: The API key of which host?
        :return:
        """

        try:
            with open(self.source, 'r') as disk:
                literal = json.load(disk)
        except OSError as err:
            raise err

        return literal[host]
