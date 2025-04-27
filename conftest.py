import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    # Создаем опции для Chrome
    options = Options()
    options.add_argument("--window-size=1200,600")  # Задаем размер окна

    # Инициализируем драйвер (путь к нему должен быть в PATH)
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()
