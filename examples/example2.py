"""

Example 1, return type based log wrapper

"""

from pandas import DataFrame
from services.log_wrapper import LogWrapper
from utils import logger


log_wrapper = LogWrapper(logger=logger)


@log_wrapper.se_logger(log_df=True, level=20)
def function_log_level_info_df() -> DataFrame:
    data_frame = DataFrame()
    return data_frame


@log_wrapper.se_logger(log_iterable=True, level=20)
def function_log_level_info_list() -> list:
    my_list = [1, 2, 3]
    return my_list


@log_wrapper.se_logger(log_iterable=True, level=20)
def function_log_level_info_dict() -> dict:
    my_dict = {"a": 1, "b": 2, "c": 3}
    return my_dict


@log_wrapper.se_logger(log_iterable=True, level=20)
def function_log_level_info_tuple() -> tuple:
    my_tuple = (1, 2, 3)
    return my_tuple


@log_wrapper.se_logger(log_iterable=True, level=20)
def function_log_level_info_set() -> set:
    my_set = {1, 2, 3}
    return my_set
