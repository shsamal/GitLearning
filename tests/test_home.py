import time
import pytest
from pageObjects.homepage import HomePage
from testData.test_data_homepage import TestData
from utilities.baseclass import BaseClass


class TestTwo_E2E_Home(BaseClass):
    def test_homepage(self, data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info(data["firstname"])
        homepage.name().send_keys(data["firstname"])
        log.info(data["email"])
        homepage.email().send_keys(data["email"])
        log.info(data["password"])
        homepage.password().send_keys(data["password"])
        homepage.checkbox().click()
        log.info(data["gender"])
        self.drop_downs(homepage.gender_dropdown(), data["gender"])
        log.info(f"{data['firstname']}{data['lastname']}")
        homepage.submit().click()
        message = homepage.message().text
        log.info(message)
        print(message)
        assert "Success! The Form has been submitted successfully!" in message

        homepage.dual_name().send_keys(data["lastname"])
        time.sleep(1)
        homepage.clear_dual_name().clear()
        homepage.driver.refresh()

        time.sleep(2)

    @pytest.fixture(params=TestData.get_testData())
    def data(self, request):
        return request.param

    # homepage.name().send_keys(data[0])
    # homepage.email().send_keys(data[1])
    # Tuple data: ("Shailaja", "shailajasamal@gmail.com", "Qwerty$#21", "Female", " Samal")
    # dict data: {"firstname": "Shailaja", "email": "shailajasamal@gmail.com",
    #                              "password": "Qwerty$#21", "gender": "Female", "lastname": " Samal"}]
