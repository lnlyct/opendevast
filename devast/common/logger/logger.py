import logging, logging.config
from threading import Thread

# __all__ = (
#     "Logger"
# )

class Logger:
    pass
    # self.handler = logging.getStreamHandler(
        
    # # )
    # self.formatter = logging.Formatter(
    #     fmt="%(asctime)s %(name)s %(levelname)s %(message)s",
    #     datefmt="[%Y-%m-%d %H:%M:%S]"
    # )

class Listener(Thread):
    """
    Listens to a shared queue as a thread 
    running from the main python process, and then
    logs all events to the console and log files.
    """

    def __init__(self, group, queue) -> None:
        """
        Params:
        group (NoneType, required) should be None; reserved for future extension when a ThreadGroup class is implemented
        queue (Queue(), required) shared queue the logger will listen to for new logs.

        Returns:
            None
        """
        self.queue = queue
        Thread.__init__(self, group, queue) # queue may not be needed here, find out by testing!

    def run(self) -> None:
        """
        TODO: Add description of run() here!
        """
        while True:
            record = self.queue.get()
            if record is None:
                break # Exits if a NoneType is sent to the queue
            logger = logging.getLogger(record.name)
            logger.handle(record)
