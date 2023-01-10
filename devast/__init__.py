# Following PEP 681
__title__ = "Devastation"
__author__ = "LonelyCat"
__description__ = "Open implementation of devast.io"
__copyright__ = "(c) 2017-present LaupaMauve"
__license__ = "See LICENSE for more details."
__version__ = "0.0.0"

from .common import database, logger, parser

cli = parser.ArgumentParser(__title__, __description__, __version__)
# args = cli.parse_args()


def run():
    pass
