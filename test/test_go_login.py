from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from curl import *
from data import Credentials
from locators import Locators


class TestLogin:
    def test_login_account(self, driver):
        driver.get(main_site)
        driver.find_element(*Locators.LOGIN_ACC_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOG_BUTTON).click()
        reg_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON)).text

        assert  reg_text == "Оформить заказ"

    def test_pers_account(self, driver):
        driver.get(main_site)
        driver.find_element(*Locators.PERS_ACC_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOG_BUTTON).click()
        reg_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON)).text

        assert reg_text == "Оформить заказ"

    def test_login_register_form(self, driver):
        driver.get(main_site)
        driver.find_element(*Locators.PERS_ACC_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.INPUT_BUTTON))
        driver.find_element(*Locators.INPUT_BUTTON).click()
        WebDriverWait(driver,3).until(EC.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOG_BUTTON).click()
        reg_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON)).text

        assert reg_text == "Оформить заказ"

    def test_login_password_recovery(self, driver):
        driver.get(main_site)
        driver.find_element(*Locators.PERS_ACC_BUTTON).click()
        driver.find_element(*Locators.RECOVER_PASSWORD).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.RECOVER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.INPUT_BUTTON))
        driver.find_element(*Locators.INPUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOG_BUTTON).click()
        reg_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON)).text

        assert  reg_text == "Оформить заказ"
