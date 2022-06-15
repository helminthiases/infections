import collections
import logging
import os
import sys

import pandas as pd


def main():

    logger.info('infections')

    # API Key
    value = src.data.keys.Keys().exc(host='who')
    logger.info(value)

    # Country codes
    try:
        frame = pd.read_csv(filepath_or_buffer=os.path.join(os.getcwd(), 'warehouse', 'gazetteer', 'countries.csv'),
                            header=0, usecols=['iso2'], dtype={'iso2': str}, encoding='utf8')
    except OSError as err:
        raise Exception(err.strerror)

    segments = frame['iso2'].to_list()
    segments = [segment for segment in segments if not pd.isnull(segment)]

    # Get prevalence data per site of country
    Parameter = collections.namedtuple(typename='Parameter', field_names=['api_key', 'disease', 'level'])
    points = src.data.points.Points(parameter=Parameter._make((value, 'sth', 'sitelevel')),
                                    fields=fields.sites)
    messages = points.exc(segments=segments)
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
    import src.data.keys
    import src.data.countries
    import src.data.units
    import src.data.points

    fields = config.Config().fields()

    main()
