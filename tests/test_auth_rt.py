import time
import pytest
from pages.auth_page import MainPage


def test_open_main_page(web_browser):
    web_browser.get('https://lk.rt.ru/')
    pages = MainPage(web_browser)
    pages.standard_auth_btn.wait_to_be_clickable().click()

    # Проверяем что в шапке есть лого
    assert pages.logo.is_presented() is not None, 'not found element'

    # Проверяем что на странице есть форма авторизации
    assert pages.form_authorization.is_presented() is not None, 'not found element'

    # Проверяем что в форме авторизации есть меню выбора типа аутентификации
    assert pages.tab_menu.is_presented() is not None, 'not found element'

    # Проверяем что в левой половине есть Продуктовый слоган ЛК "Ростелеком ID и Вспомогательная информация для клиента
    assert pages.slogan.is_presented() is not None, 'not found element'

    # Проверяем что в подвале сайта есть ссылка на пользовательское соглашение
    assert pages.agreement_link.is_presented() is not None, 'not found element'


def test_switch_tab(web_browser):
    pages = MainPage(web_browser)
    pages.standard_auth_btn.click()
    # Проверка переключения способов авторизации
    pages.tab_mail_btn.wait_to_be_clickable(5).click()
    assert pages.input_placeholder.get_text() == 'Электронная почта', 'error tab mail switch'

    pages.tab_login_btn.click()
    assert pages.input_placeholder.get_text() == 'Логин', 'error tab login switch'

    pages.tab_ls_btn.click()
    assert pages.input_placeholder.get_text() == 'Лицевой счёт', 'error ls mail switch'

    pages.tab_phone_btn.click()
    assert pages.input_placeholder.get_text() == 'Мобильный телефон', 'error phone mail switch'


# Проверка авторизации по номеру телефону с разными комбинациями входных данных
@pytest.mark.parametrize("phone", ['', 77777777777, '1000', 9185166402],
                         ids=["empty_login", "negative_login", "incorrect_login", "positive_login"])
@pytest.mark.parametrize("password", ['', "AAAAAAa@0000000000001", '1000', "AAAAAAa@000000000000"],
                         ids=["empty_password", "negative_password", "incorrect_password", 'positive_password'])
def test_login_with_phone(web_browser, phone, password):
    # Открываем главную страницу, ждем пока загрузится кнопка входа по паролю и жмем на нее
    pages = MainPage(web_browser)
    pages.standard_auth_btn.wait_to_be_clickable().click()
    pages.tab_phone_btn.click()
    # Вводим креды и жмем войти
    pages.username.send_keys(phone)
    pages.password.send_keys(password)
    pages.login_btn.click()
    # Проверка на то осуществился ли вход в ЛК
    assert pages.get_current_url() == 'https://start.rt.ru/?tab=main', 'Authorization failed!'


# Проверка авторизации по адресу электронной почты с разными комбинациями входных данных
@pytest.mark.parametrize("mail", ['', 'Mail_test_123@pp.ru', '1000', 'lady.pantelyuk@yandex.ru'],
                         ids=["empty_mail", "negative_mail", "incorrect_mail", "positive_mail"])
@pytest.mark.parametrize("password", ['', "AAAAAAa@0000000000001", '1000', "AAAAAAa@000000000000"],
                         ids=["empty_password", "negative_password", "incorrect_password", 'positive_password'])
def test_login_with_mail(web_browser, mail, password):
    # Открываем главную страницу, ждем пока загрузится кнопка входа по паролю и жмем на нее
    pages = MainPage(web_browser)
    pages.standard_auth_btn.wait_to_be_clickable().click()
    pages.tab_mail_btn.click()
    # Вводим креды и жмем войти
    pages.username.send_keys(mail)
    pages.password.send_keys(password)
    pages.login_btn.click()
    # Проверка на то осуществился ли вход в ЛК
    assert pages.get_current_url() == 'https://start.rt.ru/?tab=main', 'Authorization failed!'


# Проверка авторизации по номеру личного счета с разными комбинациями входных данных
@pytest.mark.parametrize("ls", ['', 111111111111, 'sssssssssssss', 461008743030],
                         ids=["empty_ls", "negative_ls", "incorrect_ls", "positive_ls"])
@pytest.mark.parametrize("password", ['', "AAAAAAa@0000000000001", '1000', "AAAAAAa@000000000000"],
                         ids=["empty_password", "negative_password", "incorrect_password", 'positive_password'])
def test_login_with_ls(web_browser, ls, password):
    # Открываем главную страницу, ждем пока загрузится кнопка входа по паролю и жмем на нее
    pages = MainPage(web_browser)
    pages.standard_auth_btn.wait_to_be_clickable().click()
    pages.tab_ls_btn.click()
    # Вводим креды и жмем войти
    pages.username.send_keys(ls)
    pages.password.send_keys(password)
    pages.login_btn.click()
    # Проверка на то осуществился ли вход в ЛК
    assert pages.get_current_url() == 'https://start.rt.ru/?tab=main', 'Authorization failed!'


# Проверяем что переход на выбор способа восстановления пароля возможен только для ранее зарегистрированных корректных телефонов
@pytest.mark.parametrize("phone", ['', 9913652523, '1000', 9185166402],
                         ids=["empty_phone", "negative_phone", "incorrect_phone", "positive_phone"])
def test_forget_password_open_form(web_browser, phone):
    # Открываем главную страницу, ждем пока загрузится кнопка входа по паролю и жмем на нее
    pages = MainPage(web_browser)
    pages.standard_auth_btn.wait_to_be_clickable().click()
    # Жмем забыли пароль и выбираем восстановление пароля по номеру телефона
    pages.forgot_password.click()
    pages.tab_phone_btn.click()
    # Вводим номер телефона
    pages.username.send_keys(phone)
    # Пауза на ввод капчи и нажатие на кнопку продолжить
    time.sleep(10)
    pages.reset_btn.click()
    # Проверяем что открылась нужная форма
    assert pages.reset_form_btn.is_presented() is not None, 'Form recovery not found'
    assert pages.radio_phone_btn.is_presented() is not None, 'Element not found'
    assert pages.radio_mail_btn.is_presented() is not None, 'Element not found'


# Проверяем что переход на выбор способа восстановления пароля возможен только для ранее зарегистрированных email
@pytest.mark.parametrize("mail", ['', 'Mail_test_123@pp.ru', '1000', 'lady.pantelyuk@yandex.ru'],
                         ids=["empty_mail", "negative_mail", "incorrect_mail", "positive_mail"])
def test_forget_password_with_mail_open_form(web_browser, mail):
    # Открываем главную страницу, ждем пока загрузится кнопка входа по паролю и жмем на м
    pages = MainPage(web_browser)
    pages.standard_auth_btn.wait_to_be_clickable().click()
    # Жмем забыли пароль и выбираем восстановление пароля по почте
    pages.forgot_password.click()
    pages.tab_mail_btn.click()
    # Вводим адрес почты
    pages.username.send_keys(mail)
    # Пауза на ввод капчи и нажатие на кнопку продолжить
    time.sleep(10)
    pages.reset_btn.click()
    # Проверяем что открылась нужная форма
    assert pages.reset_form_btn.is_presented() is not None, 'Form recovery not found'
    assert pages.radio_phone_btn.is_presented() is not None, 'Element not found'
    assert pages.radio_mail_btn.is_presented() is not None, 'Element not found'


# Позитивный сценарий сброса и создания нового пароля по номеру телефона
def test_forget_password_positive(web_browser):
    # Открываем главную страницу, ждем пока загрузится кнопка входа по паролю и жмем на нее
    pages = MainPage(web_browser)
    pages.standard_auth_btn.wait_to_be_clickable().click()
    # Жмем забыли пароль и выбираем восстановление пароля по номеру телефона
    pages.forgot_password.click()
    pages.tab_phone_btn.click()
    # Вводим номер телефона
    pages.username.send_keys("79185166402")
    # Пауза на ввод капчи и нажатие на кнопку продолжить
    time.sleep(10)
    pages.reset_btn.click()
    # Проверяем что открылась нужная форма
    assert pages.reset_form_btn.is_presented() is not None, 'Form recovery not found'
    assert pages.radio_phone_btn.is_presented() is not None, 'Element not found'
    # Выбор способа восстановления пароля, клик по радиобаттону
    pages.radio_phone_btn.click()
    pages.reset_form_btn.click()
    # Проверяем что открылась форма с вводом кода из смс
    assert pages.code.is_presented() is not None, 'Element not found'
    # Пауза для ввода кода из смс
    time.sleep(10)
    # Проверяем что открылась форма нового пароля
    assert pages.password_new.is_presented() is not None, 'Element not found'
    assert pages.password_confirm.is_presented() is not None, 'Element not found'
    assert pages.password_save_btn.is_presented() is not None, 'Element not found'
    # Вводим корректные данные и жмем сохранить
    pages.password_new.send_keys('Qwerty11@')
    pages.password_confirm.send_keys('Qwerty11@')
    pages.password_save_btn.click()
    # Проверяем что открылась форма авторизации с новым паролем
    assert pages.form_authorization.is_presented() is not None, 'Element not found'
    assert pages.username.get_attribute("value") == '+7 918 516-64-02'


# Проверка на корректность отображения ошибок при вводе неверного кода для сброса пароля
def test_forget_password_error_display_input_code(web_browser):
    # Открываем главную страницу, ждем пока загрузится кнопка входа по паролю и жмем на нее
    pages = MainPage(web_browser)
    pages.standard_auth_btn.wait_to_be_clickable().click()
    # Жмем забыли пароль и выбираем восстановление пароля по номеру телефона
    pages.forgot_password.click()
    pages.tab_phone_btn.click()
    # Вводим номер телефона
    pages.username.send_keys("79185166402")
    # Пауза на ввод капчи и нажатие на кнопку продолжить
    time.sleep(10)
    pages.reset_btn.click()
    # Выбор способа восстановления пароля, клик по радиобаттону
    pages.radio_phone_btn.click()
    pages.reset_form_btn.click()
    # Проверяем что открылась форма с вводом кода из смс
    assert pages.code.is_presented() is not None, 'Element not found'
    # Ждем и проверяем что появится кнопка повторного запроса пароля
    time.sleep(120)
    assert pages.resend_code_btn.is_presented() is not None, 'Element not found'
    # Запрашиваем код повторно и вводим его через 120 секунд
    pages.resend_code_btn.click()
    time.sleep(125)
    # Проверяем, что отобразится ошибка о том, что код уже устарел
    assert pages.form_error_message.is_presented() is not None, 'Element not found'
    # Запрашиваем код повторно и вводим заведомо неверный код
    pages.resend_code_btn.click()
    pages.code.send_keys("000000")
    # Проверка на то отобразилась ли соответствующая ошибка
    assert pages.error_incorrect_code.is_presented() is not None, 'Element not found'


# Проверяем, что код высылается только по зарегистрированным корректным номерам и email-ам
@pytest.mark.parametrize("login",
                         ['', 'Mail_test_123@pp.ru', '1000', 'lady.pantelyuk@yandex.ru', '', 9913652523, '1000',
                          9185166402],
                         ids=["empty_mail", "negative_mail", "incorrect_mail", "positive_mail", "empty_phone",
                              "negative_phone", "incorrect_phone", "positive_phone"])
def test_authorization_with_code(web_browser, login):
    # Открываем главную страницу
    pages = MainPage(web_browser)
    pages.wait_page_loaded()
    pages.address_login.send_keys(login)
    # Пауза для ввода капчи
    time.sleep(10)
    pages.get_code_btn.click()
    # проверяем, что появилось поле для ввода кода
    assert pages.code.is_presented() is not None, 'Element not found'


# Позитивная проверка авторизации с верным логином и кодом
@pytest.mark.parametrize("login", ['lady.pantelyuk@yandex.ru'])
def test_authorization_with_code_positive(web_browser, login):
    # Открываем главную страницу
    pages = MainPage(web_browser)
    pages.wait_page_loaded()
    pages.address_login.send_keys(login)
    # Пауза для ввода капчи
    time.sleep(10)
    pages.get_code_btn.click()
    # проверяем, что появилось поле для ввода кода
    assert pages.code.is_presented() is not None, 'Element not found'
    # Пауза для ввода кода
    time.sleep(10)
    # Проверка на то осуществился ли вход в ЛК
    assert pages.get_current_url() == 'https://start.rt.ru/?tab=main', 'Authorization failed!'


# Проверка авторизации с верным логином и неверным кодом
@pytest.mark.parametrize("login", ['lady.pantelyuk@yandex.ru'])
def test_authorization_with_incorrect_code(web_browser, login):
    # Открываем главную страницу
    pages = MainPage(web_browser)
    pages.wait_page_loaded()
    pages.address_login.send_keys(login)
    # Пауза для ввода капчи
    time.sleep(10)
    pages.get_code_btn.click()
    # Проверяем, что появилось поле для ввода кода
    assert pages.code.is_presented() is not None, 'Element not found'
    # Вводим заведомо неверный код
    pages.code.send_keys("228167")
    # Проверка на то отобразилась ли соответствующая ошибка
    assert pages.error_incorrect_code.is_presented() is not None, 'Element not found'


# Проверка регистрации с валидными данными
def test_registration(web_browser):
    # Открываем главную страницу, ждем пока загрузится кнопка входа по паролю и жмем на нее
    pages = MainPage(web_browser)
    pages.standard_auth_btn.wait_to_be_clickable().click()
    # Проверяем что есть ссылка на регистрацию и жмем
    assert pages.register_link.is_presented() is not None, 'Element not found'
    pages.register_link.click()
    # Проверяем что форма регистрации открылась корректно
    assert pages.form_registration.is_presented() is not None, 'Element not found'
    # Вводим данные
    pages.firstname_registration.send_keys('Иван')
    pages.lastname_registration.send_keys('Иванов')
    pages.address_login.send_keys('test@mail.ru')
    pages.password_registration.send_keys('QWEasd11@')
    pages.password_confirm.send_keys('QWEasd11@')
    pages.registration_btn.click()
    # Проверяем что форма ввода кода открылась корректно
    assert pages.code.is_presented() is not None, 'Element not found'
    # Пауза для ввода кода
    time.sleep(10)
    # Проверяем редирект после успешной регистрации
    assert pages.welcome_text.is_presented() is not None, 'Element not found'
    assert pages.enter_btn.is_presented() is not None, 'Element not found'


# Регистрация уже существующего пользователя
def test_registration_already_exist(web_browser):
    # Открываем главную страницу, ждем пока загрузится кнопка входа по паролю и жмем на нее
    pages = MainPage(web_browser)
    pages.standard_auth_btn.wait_to_be_clickable().click()
    # Проверяем что есть ссылка на регистрацию и жмем
    assert pages.register_link.is_presented() is not None, 'Element not found'
    pages.register_link.click()
    # Проверяем что форма регистрации открылась корректно
    assert pages.form_registration.is_presented() is not None, 'Element not found'
    # Вводим данные
    pages.firstname_registration.send_keys('Иван')
    pages.lastname_registration.send_keys('Иванов')
    pages.address_login.send_keys('test@mail.ru')
    pages.password_registration.send_keys('QWEasd11@')
    pages.password_confirm.send_keys('QWEasd11@')
    pages.registration_btn.click()
    # Проверяем что открылась форма "Учетная запись уже существует
    print(pages.user_exist.find())
    assert pages.user_exist.find() is not None, 'Element not found'
