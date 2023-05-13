from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href$='/angularpractice/shop']")
    name = (By.XPATH, "//input[@name='name']")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.XPATH, "(//input[@id='exampleInputPassword1'])[1]")
    check = (By.XPATH, "(//input[@id='exampleCheck1'])[1]")
    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    gender_option = (By.XPATH, "//option[normalize-space()='Male']")
    status = (By.XPATH, "//input[@type='radio']")
    date = (By.XPATH, "//input[@name='bday']")
    confirm = (By.XPATH, "//input[@value='Submit']")
    alert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def shop_items(self):
        return self.driver.find_element(*HomePage.shop)
        # driver.find_element(By.CSS_SELECTOR, "a[href$='/angularpractice/shop']").click()

    def enter_name(self):
        return self.driver.find_element(*HomePage.name)

    def enter_email(self):
        return self.driver.find_element(*HomePage.email)

    def enter_password(self):
        return self.driver.find_element(*HomePage.password)

    def confirm_check(self):
        return self.driver.find_element(*HomePage.check)

    def gender_options(self):
        return self.driver.find_element(*HomePage.gender)

    def select_gender(self):
        return self.driver.find_element(*HomePage.gender_option)

    def select_status(self):
        return self.driver.find_elements(*HomePage.status)

    def enter_birthdate(self):
        return self.driver.find_element(*HomePage.date)

    def confirm_button(self):
        return self.driver.find_element(*HomePage.confirm)

    def success_alert_text(self):
        return self.driver.find_element(*HomePage.alert).text


