"""

services package init file

"""

from services.log_wrapper import LogWrapper
from utils import logger

log_wrapper = LogWrapper()

__all__ = ["log_wrapper", "logger"]
