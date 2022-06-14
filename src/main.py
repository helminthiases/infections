import logging
import os
import sys


def main():

    logger.info('infections')

    value = src.data.keys.Keys().exc(host='who')
    logger.info(value)

    src.data.countries.Countries(key=value).exc()
    src.data.units.Units(key=value).exc()
    src.data.points.Points(key=value).exc(level='sitelevel',
                                          iso2_strings=['MW', 'BI', 'CM', 'CD'])


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
    import src.data.keys
    import src.data.countries
    import src.data.units
    import src.data.points

    main()
