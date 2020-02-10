import logging
logger = logging.getLogger()
logger.level = logging.DEBUG

from os.path import join, dirname

FS_DIR = join(dirname(dirname(__file__)), 'fs')
logger.debug(FS_DIR)
