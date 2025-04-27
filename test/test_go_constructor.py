from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import main_site
from locators import Locators


class TestConstructor:

    def test_transfer_filling(self, driver):
        driver.get(main_site)
        driver.find_element(*Locators.FILLING_BUTTON).click()
        filling_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.FILLING_TEXT)).text

        assert  filling_text == "Начинки"

    def test_transfer_sauces(self, driver):
        driver.get(main_site)
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        sauces_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.SAUCES_TEXT)).text

        assert  sauces_text == "Соусы"

    def test_transfer_roll(self, driver):
        driver.get(main_site)
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        driver.find_element(*Locators.ROLL_BUTTON).click()
        roll_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ROLL_TEXT)).text

        assert roll_text == "Булки"
