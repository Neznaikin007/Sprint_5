from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import *
from data import Credentials
from locators import Locators


class TestLogoutAccount:

    def test_logout(self, driver):
        driver.get(page_login)
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOG_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PERS_ACC_BUTTON))
        driver.find_element(*Locators.PERS_ACC_BUTTON).click()
        WebDriverWait(driver,3).until(EC.element_to_be_clickable(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        input_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.SIGN_IN_TRANCE)).text

        assert input_text == "Вход"
