import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s  :  %(levelname)s  :  %(funcName)s:%(lineno)d \t:\t%(message)s'
)
log = logging.getLogger()
