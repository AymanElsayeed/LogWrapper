"""

Example 3: Nested function logging levels

"""

import logging
from pandas import DataFrame
from services.log_wrapper import LogWrapper
from utils.logger import Logger

logger = Logger(logger_name="example1", log_folder="logs/example1", log_level=logging.DEBUG).logger


log_wrapper = LogWrapper(logger=logger)


@log_wrapper.se_logger(log_df=False, level=20)
def nested_function_log_levels_info_debug() -> DataFrame:

    @log_wrapper.se_logger(level=10, log_iterable=True)
    def nested_function() -> list:
        temp_list = [1, 2, 3]
        return temp_list

    nested_function()

    data_frame = DataFrame()
    return data_frame


if __name__ == "__main__":
    nested_function_log_levels_info_debug()
