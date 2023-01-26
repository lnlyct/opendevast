# Following PEP 681
__title__ = "Devastation"
__author__ = "LonelyCat"
__description__ = "Open implementation of Devastation."
__copyright__ = "(c) 2017-present LapaMauve"
__license__ = "See LICENSE for more details."
__version__ = "0.0.0"

from .common import database, logger, parser
from multiprocessing import Queue, Process
import logging

import random
import time

i = 0

def worker_process(q):
    qh = logging.handlers.QueueHandler(q)
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(qh)
    levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
              logging.CRITICAL]
    loggers = ['foo', 'foo.bar', 'foo.bar.baz',
               'spam', 'spam.ham', 'spam.ham.eggs']
    for i in range(100):
        lvl = random.choice(levels)
        logger = logging.getLogger(random.choice(loggers))
        logger.log(lvl, 'Message no. %d', i)
        time.sleep(1)

def run():
    """
    Running loop of the whole program,
    spawns any needed threads and processes.
    TODO: Run as daemon with interactive shell.
    """
    log_queue = Queue()

    # qh = logging.handlers.QueueHandler(log_queue)
    # root = logging.getLogger()
    # # root.setLevel(logging.DEBUG)
    # root.addHandler(qh)

    log_listener = logger.Listener(group=None, queue=log_queue)
    wp = Process(target=worker_process, name='worker %d' % (i + 1), args=(log_queue,))
    wp.start()
    log_listener.start()
    # Put all runtime logic in between the logger thread

    wp.join()

    log_listener.join()

