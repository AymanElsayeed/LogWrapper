"""

utilities package init file

"""

import logging
from utils.logger import Logger

logger = Logger(logger_name="example2", log_folder="logs", log_level=logging.DEBUG).logger

__all__ = ['logger',]
