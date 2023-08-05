"""

Example 1, level based log wrapper

"""

import logging
from pandas import DataFrame
from services import log_wrapper


@log_wrapper.se_logger(log_df=False, level=10)
def function_log_level_debug() -> DataFrame:
    data_frame = DataFrame()
    return data_frame


@log_wrapper.se_logger(log_df=False, level=20)
def function_log_level_info() -> DataFrame:
    data_frame = DataFrame()
    return data_frame


@log_wrapper.se_logger(log_df=False, level=30)
def function_log_level_warning() -> DataFrame:
    data_frame = DataFrame()
    return data_frame


@log_wrapper.se_logger(log_df=False, level=40)
def function_log_level_error() -> DataFrame:
    data_frame = DataFrame()
    return data_frame


@log_wrapper.se_logger(log_df=False, level=50)
def function_log_level_critical() -> DataFrame:
    data_frame = DataFrame()
    return data_frame
