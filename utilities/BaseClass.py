import inspect
import logging

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class BaseClass:

    @staticmethod
    def get_logger():  # Log record of test runs
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # Filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def verify_text_presence(self, text):
        wait_for_result = WebDriverWait(self.driver, 10)  # Slowing down the program's action
        # Verification of the correctness of the results
        wait_for_result.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

