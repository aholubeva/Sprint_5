from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.config import Config
from src.locators import BurgersLocators


class TestBurgersConstructorSection:

    def test_constructor_section_first_tab_click(self, driver):
        driver.get(Config.URL)
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.SECOND_TAB))
        driver.find_element(*BurgersLocators.SECOND_TAB).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.SECOND_TITLE))
        driver.find_element(*BurgersLocators.FIRST_TAB).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.FIRST_TITLE))
        assert 'current' in driver.find_element(*BurgersLocators.FIRST_TAB).get_attribute('class')


    def test_constructor_section_second_tab_click(self, driver):
        driver.get(Config.URL)
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.SECOND_TAB))
        driver.find_element(*BurgersLocators.SECOND_TAB).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.SECOND_TITLE))
        assert 'current' in driver.find_element(*BurgersLocators.SECOND_TAB).get_attribute('class')


    def test_constructor_section_third_tab_click(self, driver):
        driver.get(Config.URL)
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.THIRD_TAB))
        driver.find_element(*BurgersLocators.THIRD_TAB).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgersLocators.THIRD_TITLE))
        assert 'current' in driver.find_element(*BurgersLocators.THIRD_TAB).get_attribute('class')






