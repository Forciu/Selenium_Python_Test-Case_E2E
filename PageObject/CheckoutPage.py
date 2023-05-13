from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    card_title = (By.XPATH, "//div[@class='card h-100']")
    product_name_b = (By.XPATH, "./div/h4/a")
    search_name = (By.XPATH, "div//button")
    shopping_bin = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout_confirm_button = (By.XPATH, "//button[@class='btn btn-success']")

    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.card_title)

    def my_shopping_bin(self):
        return self.driver.find_element(*CheckoutPage.shopping_bin)

    def checkout_button(self):
        return self.driver.find_element(*CheckoutPage.checkout_confirm_button)
