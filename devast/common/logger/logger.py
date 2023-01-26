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

    def __init__(self, log_queue) -> None:
        # self.handler = logging.getStreamHandler(
            
        # )
        self.formatter = logging.getFormatter(
            fmt="%(asctime)s %(name)s %(levelname)s %(message)s",
            datefmt="[%Y-%m-%d %H:%M:%S]"
        )

        Thread.__init__(self, log_queue)
