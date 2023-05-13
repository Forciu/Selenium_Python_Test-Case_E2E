import pytest
from utilities.BaseClass import BaseClass
from PageObject.HomePage import HomePage
from TestData.FormSubmitData import SubmitData


class TestTwo(BaseClass):

    def test_form_submission(self, get_data):

        log = self.get_logger()

        name_input = HomePage(self.driver)  # Enter the name
        log.info("test_submission - First name is " + get_data["firstname"])

        name_input.enter_name().send_keys(get_data["firstname"])

        email_input = HomePage(self.driver)  # Enter the email
        log.info("test_submission - Email is " + get_data["email"])
        email_input.enter_email().send_keys(get_data["email"])

        password_input = HomePage(self.driver)  # Enter the password
        log.info("test_submission - Password is " + get_data["password"])
        password_input.enter_password().send_keys(get_data["password"])

        check_me = HomePage(self.driver)  # Confirm check IceCreams
        check_me.confirm_check().click()

        gender_table = HomePage(self.driver)  # Open gender table
        gender_table.gender_options().click()

        gender_select = HomePage(self.driver)  # Select gender, change on HomePage
        gender_select.select_gender().click()

        your_status = HomePage(self.driver)  # Select status
        your_status.select_status()
        status_options = your_status.select_status()

        for option in status_options:
            log.info("test_submission - Status is " + get_data["status"])
            if option.get_attribute("value") == get_data["status"]:
                option.click()
                assert option.is_selected()
                print(option)
                break

        your_birth = HomePage(self.driver)  # Enter your birthdate
        log.info("test_submission - Birthdate is " + get_data["birth"])
        your_birth.enter_birthdate().send_keys(get_data["birth"])

        form_confirmation = HomePage(self.driver)  # Confirm your form
        form_confirmation.confirm_button().click()

        success_info = HomePage(self.driver)  # Check Alert
        success_info.success_alert_text()
        success_alert = success_info.success_alert_text()
        log.info("test_submission - Success alert " + success_alert)
        assert "submitted successfully!" in success_alert
        print(success_alert)  # Confirmation of the test

        self.driver.refresh()  # Refresh page

    # Enter data for test cases
    @pytest.fixture(params=SubmitData.data_form_submission)
    def get_data(self, request):
        return request.param

    """
    # Enter data from exel for test cases
    @pytest.fixture(params=SubmitData.exel_test_data("Testcase1"))
    def get_data(self, request):
        return request.param    """

    """
    # Enter data from exel for test cases
    @pytest.fixture(params=SubmitData.exel_test_data("Testcase2"))
    def get_data(self, request):
        return request.param    """