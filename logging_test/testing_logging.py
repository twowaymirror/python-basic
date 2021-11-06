import logging
import logging.config
import sys
import json
from pathlib import Path
import pprint
import child_module
import second_child
from sub_logg import third_child
# import sub_logg.third_child as third_child

# def get_logger_test():
#     print("Testing the logging module")
#     logger = logging.getLogger(__name__)
#     logger.warning('This is a warning')

# def basic_config_test():
#     # logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
#     # logging.basicConfig(filename='example.log', level=logging.INFO)
#     logging.basicConfig(level=logging.DEBUG,format='%(levelname)s %(asctime)s %(message)s', stream=sys.stdout)
#     logging.debug('This message should go to the log file')
#     logging.info('So should this')
#     logging.warning('And this, too')
#     logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

def read_json_config():
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
        child_module.logging_test_child()
        second_child.logging_test_child()
        third_child.logging_test_third()




if __name__ == "__main__":
    print("Logging")
    read_json_config()
