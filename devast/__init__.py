# Following PEP 681
__title__ = "Devastation"
__author__ = "LonelyCat"
__description__ = "Open implementation of Devastation."
__copyright__ = "(c) 2017-present LapaMauve"
__license__ = "See LICENSE for more details."
__version__ = "0.0.0"

from .common import database, logger, parser
from multiprocessing import Queue
import logging


def run():
    """
    Running loop of the whole program,
    spawns any needed threads and processes.
    TODO: Run as daemon with interactive shell.
    """
    log_queue = Queue()
    log_listener = logger.Listener(group=None, queue=log_queue)
    log_listener.start()
    # Put all runtime logic in between the logger thread

    log_listener.join()

