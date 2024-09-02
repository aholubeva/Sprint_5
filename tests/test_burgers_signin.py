from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.config import Config
from src.locators import BurgersLocators
from src.helpers import get_sign_in_data

class TestBurgersSignIn:

    def test_sign_in_from_main_screen(self, driver):
        driver.get(Config.URL)
        email_data, password_data = get_sign_in_data()
        driver.find_element(*BurgersLocators.SIGN_IN).click()
        driver.find_element(*BurgersLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*BurgersLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*BurgersLocators.SUBMIT_BUTTON).click()
        order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
        assert order_button.is_enabled()

    def test_sign_in_from_profile_button(self, driver):
        driver.get(Config.URL)
        email_data, password_data = get_sign_in_data()
        driver.find_element(*BurgersLocators.PROFILE_BUTTON).click()
        driver.find_element(*BurgersLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*BurgersLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*BurgersLocators.SUBMIT_BUTTON).click()
        order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
        assert order_button.is_enabled()

    def test_sign_in_from_registration_button(self, driver):
        driver.get(f'{Config.URL}/register')
        email_data, password_data = get_sign_in_data()
        driver.find_element(*BurgersLocators.SIGN_IN_ALREADY).click()
        driver.find_element(*BurgersLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*BurgersLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*BurgersLocators.SUBMIT_BUTTON).click()
        order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
        assert order_button.is_enabled()

    def test_sign_in_from_forgot_password(self, driver):
        driver.get(f'{Config.URL}/forgot-password')
        email_data, password_data = get_sign_in_data()
        driver.find_element(*BurgersLocators.SIGN_IN_ALREADY).click()
        driver.find_element(*BurgersLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*BurgersLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*BurgersLocators.SUBMIT_BUTTON).click()
        order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
        assert order_button.is_enabled()


