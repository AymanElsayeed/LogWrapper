"""

Log wrapper module

"""

from __future__ import annotations
from pandas import DataFrame
import functools
from typing import Callable
from collections.abc import Iterable
from utils import logger, FunctionLoggerFilter


class LogWrapper:
    """
    Log wrapper for logging
    """

    def __init__(self, level=20):

        self.level = level

        # maps integers to logging levels

        self._logger_levels = {
            10: logger.debug,
            20: logger.info,
            30: logger.warning,
            40: logger.error,
            50: logger.critical
        }

        self._logger = self._logger_levels.get(level, logger.info)

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, level):
        self._logger = self._logger_levels.get(level, logger.info)

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
                logger_filter = FunctionLoggerFilter(func_name=function.__name__)

                logger.logger.addFilter(logger_filter)
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
                    logger.error(f"Error in {function.__name__} function: {str(ex)}")
                    raise ex
                finally:
                    logger.logger.removeFilter(logger_filter)
                    self.logger = old_level

            return wrapper

        return decorator
