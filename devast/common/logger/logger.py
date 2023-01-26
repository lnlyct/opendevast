import logging, logging.config
from threading import Thread

# __all__ = (
#     "Logger"
# )


class Logger(Thread):
    """
    Listens to a shared queue as a thread 
    running from the main python process, and then
    logs all events to the console and log files.
    """

    def __init__(self, group, log_queue) -> None:
        """
        Params:
        group (NoneType, required) should be None; reserved for future extension when a ThreadGroup class is implemented
        log_queue (Queue(), required) shared queue the logger will listen to for new logs.

        Returns:
            None
        """
        # self.handler = logging.getStreamHandler(
            
        # # )
        # self.formatter = logging.Formatter(
        #     fmt="%(asctime)s %(name)s %(levelname)s %(message)s",
        #     datefmt="[%Y-%m-%d %H:%M:%S]"
        # )
        self.log_queue = log_queue

        Thread.__init__(self, group, log_queue) # log_queue may not be needed here, find out by testing!

    def run(self):
        """
        TODO: Add description of run() here!
        """
        while True:
            record = self.log_queue.get()
            if record is None:
                break # Exits if a NoneType is sent to the queue
            logger = logging.getLogger(record.name)
            logger.handle(record)
