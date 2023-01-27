import logging, logging.config
from threading import Thread
from multiprocessing import current_process

# __all__ = (
#     "Logger"
# )

class Logger:
    """
    Instantiates a logger process,
    sends all logs to a shared queue.
    """
    def __init__(self, queue) -> None:
        """
        TODO: Add docs here!
        """
        self.logger = logging.getLogger(current_process().name)
        self.handler = logging.StreamHandler()
        self.formatter = logging.Formatter(
            fmt="%(asctime)s %(name)s %(levelname)s %(message)s",
            datefmt="[%Y-%m-%d %H:%M:%S]"
        )

        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handler)
    

    def info(self, message):
        self.logger.log(logging.INFO, message)

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
        Thread.__init__(self, group)

    def run(self) -> None:
        """
        TODO: Add description of run() here!
        """
        while True:
            record = self.queue.get()
            print(record)
            if record is None:
                break # Exits if a NoneType is sent to the queue
            log = logging.getLogger(record.name)
            print(log.hasHandlers())

    # @staticmethod
    # def configure(queue):
    #     handler = logging.handlers.QueueHandler(queue)
    #     print(current_process().name)
    #     process = current_process().name
    #     process = logging.getLogger()
    #     process.setLevel(logging.INFO)
    #     process.addHandler(handler)
