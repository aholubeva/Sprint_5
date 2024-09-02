# Sprint_5

# config.py - здесь задается URL приложения и Разрешение экрана
# helpers.py - здесь с помощью функции get_sign_up_data генерируются рандомный имя/емейл/пароль
#       get_sign_in_data - здесь сохранены емей/пароль для зарегистрированного пользователя
# locators.py - здесь описание всех используемых локаторов
# в директории tests находятся тесты для всех разделов приложения, один файл - одна функциональность
# test_burgers_signup.py - в этом файле находятся проверки для Регистрации в приложении
#       test_sign_up - проверяет успешную регистрацию с валидными данными, данные генерируется в файле  helpers.py с помощью функции get_sign_up_data
#       test_sign_up_incorrect_password - проверяет ошибку, если введен некорректный пароль
# test_burgers_signin.py - в этом файле находятся проверки для Входа в приложение
#       test_sign_in_from_main_screen - вход по кнопке «Войти в аккаунт» на главной
#       test_sign_in_from_profile_button - вход через кнопку «Личный кабинет»
#       test_sign_in_from_registration_button - вход через кнопку в форме регистрации
#       test_sign_in_from_forgot_password - вход через кнопку в форме восстановления пароля
# test_burgers_user_profile.py - в этом файле находится тест, который проверяет переход в Личный кабинет
#       test_open_user_profile - проверяет переход в Личный кабинет
# test_burgers_constructor_tab.py - в этом файле находятся проверки для Перехода из личного кабинета в конструктор 
#       test_open_constructor_tab - переход по клику на «Конструктор» 
#       test_open_constructor_tab_by_logo - переход по клику на  логотип Stellar Burgers.
# test_burgers_signout.py - в этом файле находится тест, который проверяет Выход из аккаунта
#       test_sign_out - проверяет выход из аккаунта
# test_burgers_constructor_section.py - в этом файле находятся проверки для раздела Конструктор
#       test_constructor_section_first_tab_click - проверяет переходы к разделу Булки
#       test_constructor_section_second_tab_click - проверяет переходы к разделу Соусы
#       test_constructor_section_third_tab_click - проверяет переходы к разделу Начинки

