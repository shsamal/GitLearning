from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = By.XPATH, "//a[text()='Shop']"
    first_name = By.XPATH, "(//input[@name='name'])[1]"
    email_ID = By.XPATH, "//input[@name='email']"
    pwd = By.ID, "exampleInputPassword1"
    check = By.ID, "exampleCheck1"
    gender = By.ID, "exampleFormControlSelect1"
    radio = By.XPATH, "//label[text()='Student']"
    submit_button = By.XPATH, "//input[@value='Submit']"
    success_message = By.CLASS_NAME, "alert-success"
    last_name = By.XPATH, "(//input[@name='name'])[2]"
    clear_name = By.XPATH, "(//input[@name='name'])[2]"


    def shop_items(self):
        return self.driver.find_element(*HomePage.shop)

    def name(self):
        return self.driver.find_element(*HomePage.first_name)

    def email(self):
        return self.driver.find_element(*HomePage.email_ID)

    def password(self):
        return self.driver.find_element(*HomePage.pwd)

    def checkbox(self):
        return self.driver.find_element(*HomePage.check)

    def gender_dropdown(self):
        return self.driver.find_element(*HomePage.gender)

    def radio_button(self):
        return self.driver.find_element(*HomePage.radio)

    def submit(self):
        return self.driver.find_element(*HomePage.submit_button)

    def message(self):
        return self.driver.find_element(*HomePage.success_message)

    def dual_name(self):
        return self.driver.find_element(*HomePage.last_name)

    def clear_dual_name(self):
        return self.driver.find_element(*HomePage.clear_name)
