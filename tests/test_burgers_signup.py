from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.config import Config
from src.locators import BurgersLocators
from src.helpers import get_sign_up_data

class TestBurgersSignUp:

    def test_sign_up(self, driver):
        driver.get(f'{Config.URL}/register')
        name_data, email_data, password_data, incorrect_password_data = get_sign_up_data()
        driver.find_element(*BurgersLocators.USER_NAME).send_keys(name_data)
        driver.find_element(*BurgersLocators.USER_EMAIL).send_keys(email_data)
        driver.find_element(*BurgersLocators.USER_PASSWORD).send_keys(password_data)
        driver.find_element(*BurgersLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.SUBMIT_BUTTON))
        assert  driver.current_url == f'{Config.URL}/login', "Login Url is wrong"
        driver.find_element(*BurgersLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*BurgersLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*BurgersLocators.SUBMIT_BUTTON).click()
        order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
        assert order_button.is_enabled()

    def test_sign_up_incorrect_password(self, driver):
        driver.get(f'{Config.URL}/register')
        name_data, email_data, password_data, incorrect_password_data = get_sign_up_data()
        driver.find_element(*BurgersLocators.USER_NAME).send_keys(name_data)
        driver.find_element(*BurgersLocators.USER_EMAIL).send_keys(email_data)
        driver.find_element(*BurgersLocators.USER_PASSWORD).send_keys(incorrect_password_data)
        driver.find_element(*BurgersLocators.REGISTER_BUTTON).click()
        assert driver.find_element(*BurgersLocators.INCORRECT_PASSWORD_ERROR).is_displayed()










