import time
from selenium.webdriver.common.by import By

from utilities.baseclass import BaseClass


class Confirm(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def enter_country(self):
        return self.driver.find_element(By.ID, "country")

    def get_country(self):
        # time.sleep(10)
        self.verify_explicit_wait("India")
        return self.driver.find_element(By.LINK_TEXT, "India")
        # countries = self.driver.find_elements(By.XPATH, "//div[@class='suggestions']")
        # for country in countries:
        #     if country.find_element(By.XPATH, "ul/li/a").text == "India":
        #         return country.find_element(By.XPATH, "ul/li/a")

    def check_box(self):
        return self.driver.find_element(By.XPATH, "//label[@for='checkbox2']")

    def purchase_click(self):
        return self.driver.find_element(By.XPATH, "//input[@value='Purchase']")

    def success_message(self):
        return self.driver.find_element(By.CLASS_NAME, "alert-success")
