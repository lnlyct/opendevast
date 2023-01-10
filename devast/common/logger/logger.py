import logging, logging.config
from dataclasses import dataclass

# __all__ = (
#     "Logger"
# )


@dataclass
class Colors:
    pass


@dataclass
class Styles:
    pass


class Logger:
    """
    Logs all events to the console 
    and separate instance log files.
    """

    def __init__(self, name: str) -> None:
        self.logger = logging.getLogger(name)
        # self.handler = logging.getStreamHandler(
            
        # )
        self.formatter = logging.getFormatter(
            fmt="%(asctime)s %(name)s %(levelname)s %(message)s",
            datefmt="[%Y-%m-%d %H:%M:%S]"
        )
