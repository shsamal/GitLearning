import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("/Users/shailajasamal/Documents/Selenium_data/Selenium_E2E_pytestFramework/logs/logfile.log")  # filehandler object
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # formatting style in log file.
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verify_explicit_wait(self, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located
                                             ((By.LINK_TEXT, text)))    # By.XPATH, "//div[@class='suggestions']"

    def drop_downs(self, locator, text):
        dropdown = Select(locator)  # homepage.gender_dropdown()
        dropdown.select_by_visible_text(text)   # "Female"



