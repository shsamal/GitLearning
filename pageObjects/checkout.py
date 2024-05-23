from selenium.webdriver.common.by import By
from utilities.baseclass import BaseClass


class CheckOut(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def phone_items(self):
        log = self.getLogger()
        phones = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for i in phones:
            log.info(i.find_element(By.XPATH, "div/h4/a").text)
        for phone in phones:
            if phone.find_element(By.XPATH, "div/h4/a").text == "iphone X":
                return phone.find_element(By.XPATH, "div/button")

    def add_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary")

    def checkout(self):
        return self.driver.find_element(By.CLASS_NAME, "btn-success")

