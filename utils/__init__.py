"""

utilities package init file

"""

import logging
from utils.logger import Logger, FunctionLoggerFilter

logger = Logger(logger_name="example2", log_folder="logs", log_level=logging.DEBUG).logger

__all__ = ['logger', 'FunctionLoggerFilter']
