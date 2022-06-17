import os
import logging
import glob


def main():

    path = os.path.join(os.getcwd(), 'warehouse', 'data', 'sitelevel')

    items = glob.glob(pathname=os.path.join(path, '*.csv'))

    for item in items:
        logger.info(item)


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    main()
