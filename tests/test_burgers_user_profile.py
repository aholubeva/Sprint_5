from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.config import Config
from src.locators import BurgersLocators
from src.helpers import get_sign_in_data

class TestBurgersUserProfile:

    def test_open_user_profile(self, driver):
        driver.get(Config.URL)
        email_data, password_data = get_sign_in_data()
        driver.find_element(*BurgersLocators.SIGN_IN).click()
        driver.find_element(*BurgersLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*BurgersLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*BurgersLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.ORDER_BUTTON))
        driver.find_element(*BurgersLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.PROFILE_LINK))
        assert driver.current_url == f'{Config.URL}/account/profile', "Profile Url is wrong"
