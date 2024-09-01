from selenium.webdriver.common.by import By

class BurgersLocators:
    PROFILE_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']" # Личный кабинет кнопка
    REGISTER_LINK = By.XPATH, "//a[text()='Зарегистрироваться']" # Ссылка на регистрацию
    USER_NAME = By.XPATH, "//label[text() = 'Имя']/following-sibling::input" # Поле "Имя" нового юзера
    USER_EMAIL = By.XPATH, "//label[text() = 'Email']/following-sibling::input" # Поле "Email" нового юзера
    USER_PASSWORD = By.XPATH, "//label[text() = 'Пароль']/following-sibling::input" # Поле "Пароль" нового юзера
    REGISTER_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']" # Кнопка "Зарегистрироваться"
    EMAIL_FIELD = By.XPATH, "//label[text() = 'Email']/following-sibling::input" # Поле Email для существующего юзера
    PASSWORD_FIELD = By.XPATH, "//label[text() = 'Пароль']/following-sibling::input" # Поле Пароль для существующего юзера
    SUBMIT_BUTTON = By.XPATH, "//button[text()='Войти']" # Кнопка Войти для существующего юзера
    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выход']" # Кнопка Выход для существующего юзера
    INCORRECT_PASSWORD_ERROR = By.XPATH, "//p[text()='Некорректный пароль']" # Ошибка при некорректном пароле
    SIGN_IN = By.XPATH, "//button[text()='Войти в аккаунт']" # Кнопка Войти в аккаунт с главной страницы
    ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']" # Кнопка Оформить заказ на главной странице
    SIGN_IN_ALREADY = By.XPATH, "//a[text()='Войти']" # Кнопка Войти под формой Регистрации
    PROFILE_LINK = By.XPATH, "//a[text()='Профиль']" # Кнопка Личный кабинет в хедере
    CONSTRUCTOR_TAB = By.XPATH, "//p[text()='Конструктор']" # Таба Конструктор в хедере
    CONSTRUCTOR_LOGO = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]" # Лого в хедере
    FIRST_TAB = By.XPATH, "//span[text()='Булки']" # Таба Булки
    FIRST_TITLE = By.XPATH, "//h2[text()='Булки']" # Заголовок Булки
    SECOND_TAB = By.XPATH, "//span[text()='Соусы']" # Таба Соусы
    SECOND_TITLE = By.XPATH, "//h2[text()='Соусы']" # Заголовок Соусы
    THIRD_TAB = By.XPATH, "//span[text()='Начинки']" # Таба Начинки
    THIRD_TITLE = By.XPATH, "//h2[text()='Начинки']" # Заголовок Начинки


