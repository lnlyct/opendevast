# Following PEP 681
__title__ = "Devastation"
__author__ = "LonelyCat"
__description__ = "Open implementation of Devastation."
__copyright__ = "(c) 2017-present LapaMauve"
__license__ = "See LICENSE for more details."
__version__ = "0.0.0"

from .common import database, logger, parser
from multiprocessing import Queue


def run():
    """
    Running loop of the whole program,
    spawns any needed threads and processes.
    TODO: Run as daemon with interactive shell.
    """
    log_queue = Queue()
    log = logger.Logger(group=None, log_queue=log_queue)
    log.start()
    log.join()

