import time
from pageObjects.checkout import CheckOut
from pageObjects.confirmpage import Confirm
from pageObjects.homepage import HomePage
from utilities.baseclass import BaseClass


class TestOne_E2E_Purchase(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.shop_items().click()  # //a[@href="/angularpractice/shop"]
        log.info("The phones are: ")

        checkout = CheckOut(self.driver)
        checkout.phone_items().click()
        checkout.add_cart().click()
        checkout.checkout().click()

        confirm = Confirm(self.driver)
        confirm.enter_country().send_keys("ind")
        country = confirm.enter_country().get_attribute("value")
        log.info(country)
        confirm.get_country().click()

        # countries = driver.find_elements(By.XPATH, "//div/ul/li/a")
        # for country in countries:
        #     if country.text == "India":
        #         country.click()

        confirm.check_box().click()
        confirm.purchase_click().click()
        alert_message = confirm.success_message().text
        log.info(alert_message)
        print(alert_message)
        assert "Success!" in alert_message

        time.sleep(2)


