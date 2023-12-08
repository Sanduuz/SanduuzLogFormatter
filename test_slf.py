#!/usr/bin/env python3

"""
Import Sanduuz Log Formatter (SLF) as a module and test it's capabilities.
"""

import logging
from sanduuzlogformatter import SLF

formatter = SLF()

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


# 17 characters
def even_shorter_name(message: str) -> None:
    logger.info(message)


# 26 characters
def function_with_shorter_name(message: str) -> None:
    logger.info(message)


# 36 characters
def function_with_a_relatively_long_name(message: str) -> None:
    logger.info(message)


# 46 characters
def function_with_a_really_really_really_long_name(message: str) -> None:
    logger.info(message)


# 77 characters
def function_with_a_really_long_super_duper_name_used_purely_for_testing_purposes(message: str) -> None:
    logger.info(message)


def main():
    """ Test different debug levels and functions. """
    logger.debug("This is a test message.")
    logger.info("This is a test message.")
    logger.warning("This is a test message.")
    logger.error("This is a test message.")
    logger.critical("This is a test message.")
    even_shorter_name("This is a test message.")
    function_with_shorter_name("This is a test message.")
    function_with_a_relatively_long_name("This is a test message.")
    function_with_a_really_really_really_long_name("This is a test message.")
    function_with_a_really_long_super_duper_name_used_purely_for_testing_purposes("This is a test message.")


if __name__ == '__main__':
    main()
