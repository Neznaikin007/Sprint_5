from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import main_site
from data import Credentials
from locators import Locators


class TestPersonalAccount:

    def test_transfer_account(self, driver):
        driver.get(main_site)
        driver.find_element(*Locators.PERS_ACC_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOG_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PERS_ACC_BUTTON))
        driver.find_element(*Locators.PERS_ACC_BUTTON).click()
        reg_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TEXT_PROFILE)).text

        assert reg_text == "Профиль"
