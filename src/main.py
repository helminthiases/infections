"""
The main module for running other classes
"""
import logging
import os
import sys


def main():
    """
    Entry point

    :return: None
    """

    logger.info('infections')

    src.helminth.countries.Countries().exc()


if __name__ == '__main__':
    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    import src.helminth.countries

    main()
