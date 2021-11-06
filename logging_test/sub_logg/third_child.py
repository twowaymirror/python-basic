import logging
import logging.config
import json
import pprint
from pathlib import Path

logger = logging.getLogger(__name__)

def logging_test_child():
    print("Testing the logging module")
    # logger.setLevel("WARNING")
    logger.info(f"This is name: {__name__}")
    logger.warning('This is a warning')
    logger.debug('This message should go to the log file')
    logger.info('So should this')
    logger.warning('And this, too')
    logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

def logging_test_third():
    print(f"Testing to use a json config file")
    with open("logging.json", "rt") as js:
        config = json.load(js)
        pprint.pprint(config)
        logging.config.dictConfig(config)

        logger = logging.getLogger(__name__)
        # logger = logging.getLogger(__name__)
        print(f'This is the name: {__name__}')
        logger.debug('This message should go to the log file')
        logger.info('So should this')
        logger.warning('And this, too')
        logger.error('And non-ASCII stuff, too, like Øresund and Malmö')


if __name__ == "__main__":
    print("Logging")
    # read_json_config()
