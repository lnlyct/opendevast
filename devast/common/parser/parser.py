import argparse
from typing import Optional, Required

__all__ = (
    "ArgumentParser",
    "ConfigParser"
)

class ArgumentParser:
    """
    Parses any command line arguments that are given
    to the parent python process. Arguments are returned
    as a dictionary.

    This class is reserved for the parent __init__ process,
    however the arguments the parents invokes to the parser are
    made available to the rest of the program via a classmethod.
    """

    args = dict # cls accessible dict for any internal modules to view cmdline args passed to parent process

    def __init__(self, __title__: Required[str], __description__: Required[str], __version__: Required[str]) -> None:
        """
        Params:
        __title__ (str, required) parent process name
        __description__ (str, required) parent process description
        __version__ (str, required) parent process version

        Returns:
            None
        """
        self.argparser = argparse.ArgumentParser(
            prog = __title__,
            description = __description__,
            epilog = __version__
        )
        self.argparser.add_argument()


class ConfigParser:
    """
    Parses requested parts of a given .ini file
    and returns all configurations asked for.
    Optionally looks for a build flag, defaults to dev.
    Build flag affects config vars returned from .ini!

    While the parser doesn't require any params to init,
    its important to understand this is just to make the
    end users life a bit easier. Any core components of the
    program must pass in the available params or risk the parser
    reading the wrong configuration file and running 
    in the default build mode by default!
    """

    def __init__(self, conf: Optional[str], build: Optional[str] = "dev") -> None:
        """
        Params:
            conf (str, optional): .ini configuration file absolute path.
            build (str, optional): build runtime type for parent program
        
        Returns: 
            None
        """
        
        self.conf: Optional[str] = conf
        self.build: Optional[str] = build

