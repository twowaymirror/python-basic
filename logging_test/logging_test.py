import logging
import sys

def get_logger_test():
    print("Testing the logging module")
    logger = logging.getLogger(__name__)
    logger.warning('This is a warning')

def basic_config_test():
    # logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    # logging.basicConfig(filename='example.log', level=logging.INFO)
    logging.basicConfig(level=logging.DEBUG,format='%(levelname)s %(asctime)s %(message)s', stream=sys.stdout)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

if __name__ == "__main__":
    print("Logging")
    basic_config_test()