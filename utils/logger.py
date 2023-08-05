"""

Logger class.

"""

import logging
import os
import pathlib
from logging.handlers import TimedRotatingFileHandler


__all__ = ['LoggerFilter', 'Logger']
LOGLEVEL = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]


class LoggerFilter(logging.Filter):
    """
    Logger filter for logging
    Update application name, username and session id for log record
    :param user_name: username
    :type user_name: str
    :param session_id: session id
    :type session_id: str
    :param app_name: application name
    :type app_name: str
    """

    def __init__(self, user_name, session_id, app_name):
        super().__init__()
        self.user_name = user_name
        self.session_id = session_id
        self.app_name = app_name

    def filter(self, record: logging.LogRecord):
        """
        Add record attributes to logging format.
        :param record: record object
        :type record: logging.LogRecord
        :return: Boolean
        """
        record.app_name = self.app_name
        record.user_name = self.user_name
        record.session_id = self.session_id
        return True


class Logger:

    def __init__(self, logger_name: str, log_folder: str, log_level: int):
        """
        logger class
        :param logger_name: logger name
        :type logger_name: str
        :param log_folder: log folder
        :type log_folder: str
        :param log_level: log level
        :type log_level: int
        """
        if log_level not in LOGLEVEL:
            raise ValueError(f"Log level must be one of {LOGLEVEL}")

        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)
        if not os.path.isdir(log_folder):
            os.makedirs(log_folder)

        log_format = '[%(asctime)s] [%(levelname)s] [%(user_name)s] [%(app_name)s] [%(funcName)s] [%(session_id)s] - %(message)s'
        self.full_file_path = pathlib.Path(log_folder).absolute().joinpath(f"{logger_name}.log").as_posix()
        if not os.path.isfile(self.full_file_path):
            with open(self.full_file_path, mode="a", encoding='utf8') as _:
                pass

        logger_file = TimedRotatingFileHandler(filename=self.full_file_path, when="midnight", interval=1,
                                               encoding="utf-8-sig")
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(log_format))
        console_handler.setLevel(logging.DEBUG)

        logger_file.setFormatter(logging.Formatter(log_format))
        self.logger.addHandler(logger_file)

        self.logger.addHandler(console_handler)

        # logger.propagate = False
        logger_extra = {'user_name': 'Ayman', 'app_name': 'app', 'session_id': '1024'}
        self.logger = logging.LoggerAdapter(self.logger, logger_extra)
        # self.logger.logger.addFilter(LoggerFilter(user_name="SYSTEM", session_id="Ayman", app_name="app"))
