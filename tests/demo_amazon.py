from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//span[text()='Fresh']").click()



time.sleep(2)