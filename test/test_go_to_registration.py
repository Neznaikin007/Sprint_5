from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestRegistrationNewUser:

    def test_successful_registration(self, driver):
        driver.get(main_site)
        driver.find_element(*Locators.PERS_ACC_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.REG_LINK))
        driver.find_element(*Locators.REG_LINK).click()
        name, email, password = generate_registration_data()
        WebDriverWait(driver, 5).until((EC.visibility_of_element_located(Locators.NAME)))
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        reg_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SIGN_IN_TRANCE)).text

        assert reg_text == 'Вход'


class TestCheckingCreationNonExistentAccount:

    def test_failed_registration(self, driver):
        driver.get(main_site)
        driver.find_element(*Locators.PERS_ACC_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.REG_LINK))
        driver.find_element(*Locators.REG_LINK).click()
        WebDriverWait(driver, 5).until((EC.visibility_of_element_located(Locators.NAME)))
        driver.find_element(*Locators.NAME).send_keys(Credentials.name)
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(12345)
        driver.find_element(*Locators.REG_BUTTON).click()
        reg_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_PASSWORD)).text

        assert reg_text == 'Некорректный пароль'
