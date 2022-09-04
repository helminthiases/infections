"""
The main module for running other classes
"""
import glob
import logging
import os
import sys

import pandas as pd


def main():
    """
    Entry point

    :return: None
    """

    logger.info('infections')

    message = src.data.countries.Countries().exc()
    logger.info(message)

    messages = src.data.experiments.Experiments().exc()
    logger.info(messages)

    # The project's experiments data
    files = glob.glob(pathname=os.path.join(root, 'warehouse', 'data', 'ESPEN', 'experiments', 'reduced', '*.csv'))
    elements = [file.split('helminthiases', 1)[1] for file in files]
    elements = [element.replace('\\', '/') for element in elements]
    elements = [hub + element for element in elements]

    data = pd.DataFrame(data={'path': elements})
    data.to_csv(path_or_buf=os.path.join(root, 'warehouse', 'data', 'ESPEN', 'experiments', 'data.csv'),
                index=False, header=True, encoding='utf-8')


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))
    hub = 'https://raw.githubusercontent.com/helminthiases'

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Libraries
    import src.data.countries
    import src.data.experiments
    import src.experiments.equivalent

    main()
