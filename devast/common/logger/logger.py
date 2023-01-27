import logging, logging.config, logging.handlers
from threading import Thread
from multiprocessing import current_process

# __all__ = (
#     "Logger"
# )

# class Logger:
#     """
#     Instantiates a logger process,
#     sends all logs to a shared queue.
#     """
#     def __init__(self, process, queue) -> None:
#         """
#         TODO: Add docs here!
#         """
#         self.queue = queue
#         self.logger = logging.getLogger(process)
#         self.handler = logging.handlers.QueueHandler(queue)
#         # self.formatter = logging.Formatter(
#         #     fmt="%(asctime)s %(name)s %(levelname)s %(message)s",
#         #     datefmt="[%Y-%m-%d %H:%M:%S]"
#         # )

#         self.logger.setLevel(logging.DEBUG)
#         self.logger.addHandler(self.handler)

    # @staticmethod
    

    # def info(self, message):
    #     self.logger.log(logging.INFO, message)

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

    @staticmethod
    def configure(queue):
        print(current_process().name)
        handler = logging.handlers.QueueHandler(queue)
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        root.addHandler(handler)
