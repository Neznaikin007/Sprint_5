from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import *
from data import Credentials
from locators import Locators


class TestTransferToConstructor:

    def test_transfer_constructor(self, driver):
        driver.get(main_site)
        driver.find_element(*Locators.LOGIN_ACC_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOG_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERS_ACC_BUTTON))
        driver.find_element(*Locators.PERS_ACC_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        burger_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TEXT_BURGER)).text

        assert burger_text == "Соберите бургер"

    def test_transfer_stellar_burgers(self, driver):
        driver.get(page_login)
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOG_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERS_ACC_BUTTON))
        driver.find_element(*Locators.PERS_ACC_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGO_ST_BURGERS))
        driver.find_element(*Locators.LOGO_ST_BURGERS).click()
        burger_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TEXT_BURGER)).text

        assert burger_text == "Соберите бургер"
