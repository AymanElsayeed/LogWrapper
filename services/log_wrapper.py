"""

Log wrapper module

"""

from __future__ import annotations
import logging
from pandas import DataFrame
import functools
from typing import Callable
from collections.abc import Iterable


class FunctionLoggerFilter(logging.Filter):
    """
    Logger filter for logging
    Update function name for log record
    :param func_name: function name
    """

    def __init__(self, func_name):
        super().__init__()
        self.func_name = func_name

    def filter(self, record: logging.LogRecord):
        """
        Add record attributes to logging format.
        :param record: record object
        :type record: logging.LogRecord
        :return: Boolean
        """
        record.funcName = self.func_name
        return True


class LogWrapper:
    """
    Log wrapper for logging
    """

    def __init__(self, logger: logging.Logger, level=20):

        self.level = level
        self.log = logger

        # maps integers to logging levels

        self._logger_levels = {
            10: self.log.debug,
            20: self.log.info,
            30: self.log.warning,
            40: self.log.error,
            50: self.log.critical
        }

        self._logger = self._logger_levels.get(level, self.log.info)

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, level):
        self._logger = self._logger_levels.get(level, self.log.info)

    def data_frame_logger(self, data_frame: DataFrame):
        self.logger(f"Data Frame Shape: {data_frame.shape}")
        self.logger(f"Data Frame Dtypes: {data_frame.dtypes}")
        self.logger(f"Data Frame Head: {data_frame.head()}")
        self.logger(f"Data Frame Columns: {data_frame.columns.to_list()}")

    def se_logger(self, log_df=False, level=10, log_iterable=False) -> Callable:
        """
        Log wrapper for logging
        :return: function
        """
        old_level = self.level
        # old_level = logger.logger.level
        self.logger = level

        def decorator(function: Callable):
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                """
                Wrapper function
                :param args: arguments
                :type args: tuple
                :param kwargs: keyword arguments
                :type kwargs: dict
                :return: function
                """
                self.logger = level
                module_name = module_name = function.__module__.split(".")[-1]
                function_name = function.__name__
                logger_filter = FunctionLoggerFilter(func_name=f"{module_name}.{function_name}")

                self.log.logger.addFilter(logger_filter)
                start_message = f"Starting function"
                finish_function = f"Finished function"

                try:
                    self.logger(start_message)

                    results = function(*args, **kwargs)

                    is_dataframe = isinstance(results, DataFrame)
                    is_iterable = isinstance(results, Iterable)

                    if log_df and is_dataframe:
                        self.data_frame_logger(results)

                    if log_iterable and is_iterable:
                        self.logger(f"Iterable: {type(results)}")
                        self.logger(f"Iterable: {len(results)}")

                    self.logger(finish_function)
                except Exception as ex:
                    self.log.error(f"Error in {function.__name__} function: {str(ex)}")
                    raise ex
                finally:
                    self.log.logger.removeFilter(logger_filter)
                    self.logger = old_level

            return wrapper

        return decorator
