# Following PEP 681
__title__ = "Devastation"
__author__ = "LonelyCat"
__description__ = "Open implementation of Devastation."
__copyright__ = "(c) 2017-present LapaMauve"
__license__ = "See LICENSE for more details."
__version__ = "0.0.0"

from .common import database, logger, parser
from multiprocessing import Queue, Process, current_process
import logging

import time
def worker_process(log_queue):
    # logger.Listener.configure(log_queue)    
    logg = logger.Logger(log_queue)

    while True:
        logg.info("hewo")
        time.sleep(1)

def run():
    """
    Running loop of the whole program,
    spawns any needed threads and processes.
    TODO: Run as daemon with interactive shell.
    """
    log_queue = Queue(-1)
    # logger.Listener.configure(log_queue) # Main process logging, for some reason is eternal loop
    wp = Process(target=worker_process, args=(log_queue,))
    wp.start()

    log_listener = logger.Listener(group=None, queue=log_queue)
    log_listener.start()
    wp.join()
    log_queue.put(None)
    log_listener.join()
