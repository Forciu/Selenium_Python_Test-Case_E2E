from utilities.BaseClass import BaseClass
from PageObject.HomePage import HomePage
from PageObject.CheckoutPage import CheckoutPage
from PageObject.ConfirmPage import ConfirmPage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)  # Entering the shop tab
        home_page.shop_items().click()

        checkout_page = CheckoutPage(self.driver)  # Searching for a product cards
        products = checkout_page.get_card_titles()
        for product in products:  # Searching for a specific product in the product cards
            product_name = product.find_element(*CheckoutPage.product_name_b).text
            log.info("test_e2e - getting the card title - " + product_name)
            if product_name == "Blackberry":
                product.find_element(*CheckoutPage.search_name).click()

        shop_bin = CheckoutPage(self.driver)  # Entering my shopping bin
        shop_bin.my_shopping_bin().click()

        bin_button = CheckoutPage(self.driver)  # Button to confirm the desire to purchase
        bin_button.checkout_button().click()

        delivery_address = ConfirmPage(self.driver)  # Entering the delivery address
        log.info("test_e2e - Entering country name as Pol")
        delivery_address.select_country().send_keys("Pol")
        self.verify_text_presence("Poland")  # Verification text, change on ConfirmPage

        check_delivery_address = ConfirmPage(self.driver)  # Selecting an address
        check_delivery_address.check_delivery().click()

        confirm_conditions = ConfirmPage(self.driver)  # Confirmation conditions
        confirm_conditions.accept_conditions().click()

        confirm_purchase = ConfirmPage(self.driver)  # Making a purchase
        confirm_purchase.purchase().click()

        alert_success_text = confirm_purchase.get_success_alert_text()  # Asert check after purchase
        log.info("test_e2e - Text received from application is "+alert_success_text)
        assert "Success! Thank you!" in alert_success_text

        """Line to check correct operation of screenshot capture if error occurs"""
        # assert "Success! Thank mee!" in alert_success_text #
        print(alert_success_text)  # Confirmation of the test

