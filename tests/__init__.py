import logging
import sys
from os.path import join, dirname

stream_handler = logging.StreamHandler(sys.stdout)

logger = logging.getLogger()
logger.level = logging.DEBUG


TEST_DATA_DIR = join(dirname(__file__), 'data')


def print_request(logger, req):
    logger.debug('\n{}\n{}\n{}\nBODY SIZE: {}\n'.format(
        '-----------BEGIN REQUEST-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        len(req.body) if req.body is not None else None,
    ))
