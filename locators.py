from selenium.webdriver.common.by import By


class Locators:

    PERS_ACC_BUTTON = [By.XPATH, ".//p[text()='Личный Кабинет']"]                       # Кнопка Личный кабинет
    REG_LINK = [By.XPATH, ".//a[text()='Зарегистрироваться']"]                          # Вы новый пользователь? Кнопка Зарегистрироваться
    NAME = [By.XPATH, ".//div[label[contains(text(), 'Имя')]]//input"]                  # Поле Имя
    EMAIL= [By.XPATH, ".//div[label[contains(text(), 'Email')]]//input"]                # Поле Email
    PASSWORD = [By.XPATH, ".//input[@name='Пароль']"]                                   # Поле Пароль
    REG_BUTTON = [By.XPATH, ".//button[text()='Зарегистрироваться']"]                   # Кнопка Зарегистрироваться в форме регистрации
    ERROR_PASSWORD = [By.XPATH, ".//p[text()='Некорректный пароль']"]                   # Текст "Некорректный пароль" у поля Пароль
    SIGN_IN_TRANCE = [By.XPATH, ".//h2[text()='Вход']"]                                 # Текст "Вход" на странице Авторизации


    LOGIN_ACC_BUTTON = [By.XPATH, ".//button[text()='Войти в аккаунт']"]                    # Кнопка Войти в аккаунт

    LOG_BUTTON = [By.XPATH, ".//button[text()='Войти']"]                                    # Кнопка Войти на странице Авторизации
    PLACE_AN_ORDER_BUTTON = [By.XPATH, ".//button[text()='Оформить заказ']"]                # Кнопка Оформить заказ
    RECOVER_PASSWORD = [By.XPATH, ".//a[text()='Восстановить пароль']"]                     # Забыл пароль? Кнопка Восстановить пароль
    RECOVER_BUTTON = [By.XPATH, ".//form[button[contains(text(), 'Восстановить')]]"]        # Кнопка Восстановить
    INPUT_BUTTON = [By.XPATH, ".//a[text()='Войти']"]                                       # Вспомнили пароль? Кнопка Войти
    TEXT_PROFILE = [By.XPATH, ".//a[text()='Профиль']"]                                     # Текст Профиль в Личном Кабинете
    CONSTRUCTOR_BUTTON = [By.XPATH, ".//p[text()='Конструктор']"]                           # Кнопка Конструктор
    TEXT_BURGER = [By.XPATH, ".//h1[text()='Соберите бургер']"]                             # Текст Соберите бургер
    LOGO_ST_BURGERS = [By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]/a"]    # Текст Логотипа Stellar Burgers
    EXIT_BUTTON = [By.XPATH, ".//li[3]//button[text()='Выход']"]                            # Кнопка Выход в Личном Кабинете
    FILLING_BUTTON = [By.XPATH, ".//span[text()='Начинки']"]                                # Кнопка Начинки
    FILLING_TEXT = [By.XPATH, ".//h2[3][text()='Начинки']"]                                 # Текст Начинки в разделе Соберите бургер
    SAUCES_BUTTON = [By.XPATH, ".//span[text()='Соусы']"]                                   # Кнопка Соусы
    SAUCES_TEXT = [By.XPATH, ".//h2[2][text()='Соусы']"]                                    # Текст Соусы в разделе Соберите бургер
    ROLL_BUTTON = [By.XPATH, ".//span[text()='Булки']"]                                     # Кнопка Булки
    ROLL_TEXT = [By.XPATH, ".//h2[1][text()='Булки']"]                                      # Текст Булки в разделе Соберите бургер