from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country_selection = (By.XPATH, "//input[@id='country']")
    confirm_delivery = (By.LINK_TEXT, "Poland")
    conditions = (By.XPATH, "//label[@for='checkbox2']")
    purchase_button = (By.CSS_SELECTOR, "input[value='Purchase']")
    alert = (By.CLASS_NAME, "alert-success")

    def select_country(self):
        return self.driver.find_element(*ConfirmPage.country_selection)

    def check_delivery(self):
        return self.driver.find_element(*ConfirmPage.confirm_delivery)

    def accept_conditions(self):
        return self.driver.find_element(*ConfirmPage.conditions)

    def purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def get_success_alert_text(self):
        return self.driver.find_element(*ConfirmPage.alert).text
