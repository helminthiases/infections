import collections
import logging
import os
import sys

import pandas as pd


def main():

    logger.info('infections')

    # API Key
    value = src.helminth.keys.Keys().exc(host='who')
    logger.info(value)

    # Country codes
    try:
        frame = pd.read_csv(filepath_or_buffer=os.path.join(os.getcwd(), 'warehouse', 'gazetteer', 'countries.csv'),
                            header=0, usecols=['iso2'], dtype={'iso2': str}, encoding='utf8')
    except OSError as err:
        raise Exception(err.strerror)
    codes = frame['iso2'].to_list()
    codes = [code for code in codes if not pd.isnull(code)]

    # Get prevalence data per site of country
    parameters = [{'api_key': value, 'disease': 'sth', 'level': 'sitelevel', 'iso2': iso2} for iso2 in codes]
    points = src.helminth.points.Points(level='sitelevel', fields=fields.sites)
    messages = points.exc(parameters=parameters)
    logger.info(messages)


if __name__ == '__main__':

    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # libraries
    import config
    import src.helminth.keys
    import src.helminth.countries
    import src.helminth.units
    import src.helminth.points

    fields = config.Config().fields()

    main()
