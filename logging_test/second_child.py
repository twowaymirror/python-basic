import logging
import logging.config
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


if __name__ == "__main__":
    print("Logging")
    # read_json_config()
