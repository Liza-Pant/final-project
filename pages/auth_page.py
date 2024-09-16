import os

from pages.base import WebPage
from pages.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://lk.rt.ru/'

        super().__init__(web_driver, url)

    # Ввод логина
    username = WebElement(id='username')

    # Ввод пароля
    password = WebElement(id='password')

    # Кнопка войти
    login_btn = WebElement(xpath='//button[@name="login"]')

    # Кнопка войти по временному коду
    back_to_otp_btn = WebElement(xpath='//button[@name="back_to_otp_btn"]')

    # Кнопка войти c паролем
    standard_auth_btn = WebElement(id='standard_auth_btn')

    # Кнопка получить код
    get_code_btn = WebElement(id='otp_get_code')

    # Ссылка на регистрацию
    register_link = WebElement(id='kc-register')

    # Ссылка Забыл пароль
    forgot_password = WebElement(id='forgot_password')

    # Меню способов авторизации, вкладка телефон
    tab_phone_btn = WebElement(id='t-btn-tab-phone')

    # Меню способов авторизации, вкладка почта
    tab_mail_btn = WebElement(id='t-btn-tab-mail')

    # Меню способов авторизации, вкладка логин
    tab_login_btn = WebElement(id='t-btn-tab-login')

    # Меню способов авторизации, вкладка лицевой счет
    tab_ls_btn = WebElement(id='t-btn-tab-ls')

    # Ввод телефона или почты для логина по коду
    address_login = WebElement(xpath='//input[@id="address"]')

    # Плейсхолдер в поле ввода username
    input_placeholder = WebElement(xpath='//div[@class=\"tabs-input-container\"]//span[@class="rt-input__placeholder"]')

    # Лого в шапке сайта
    logo = WebElement(
        xpath='//div[@class="main-header__logo-container"]')
    # Форма авторизации
    form_authorization = WebElement(
        xpath='//div[@class="card-container login-form-container login-form-container"]')

    # Меню смены способа авторизации
    tab_menu = WebElement(
        xpath='//div[@class="card-container login-form-container login-form-container"]//div[@class="rt-tabs rt-tabs--orange rt-tabs--small tabs-input-container__tabs"]')

    # Слоган
    slogan = WebElement(
        xpath='//section[@id="page-left"]/div[@class="what-is-container"]')

    # Ссылка на пользовательское соглашение
    agreement_link = WebElement(
        xpath='//footer[@id="app-footer"]//a[@class="rt-footer-agreement-link"]')

    # Кнопка продолжить в сбросе пароля
    reset_btn = WebElement(id='reset')

    # Форма выбора способа восстановления пароля
    form_reset = WebElement(
        xpath='//div[@class="card-container__wrapper"]/h1[contains(text(), "Восстановление пароля")]')

    # Кнопка продолжить подтверждение сброса пароля
    reset_form_btn = WebElement(id='reset-form-submit')

    # Радиокнопка по номеру телефона
    radio_phone_btn = WebElement(xpath='//label[@id="sms-reset-type"]//span[@class="rt-radio__circle"]')

    # Радиокнопка по email
    radio_mail_btn = WebElement(xpath='//label[@id="email-reset-type"]//span[@class="rt-radio__circle"]')

    # ПЕРВОЕ поле для ввода кода из смс для сброса пароля
    code = WebElement(xpath='//input[@id="rt-code-input"]')

    # Кнопка повторного запроса кода из смс для сброса пароля
    resend_code_btn = WebElement(xpath='//button[@id="otp-resend-code"]')

    # Срок действия пароля истек
    form_error_message = WebElement(
        xpath='//span[@id="form-error-message" and contains(text(), "Срок действия кода истёк. Пожалуйста, запросите код снова")]')

    # Ввод нового пароля
    password_new = WebElement(id='password-new')

    # Форма авторизации по коду
    form_authorization_code = WebElement(
        xpath='//div[@class="card-container__wrapper"]/h1[contains(text(), "Авторизация по коду")]')

    # Повтор нового пароля
    password_confirm = WebElement(id='password-confirm')

    # Кнопка сохранения пароля
    password_save_btn = WebElement(id='t-btn-reset-pass')

    # Поле с введенным значением в поле username
    username_value = WebElement(xpath='//input[@type="hidden" and @name="username"]')

    # Отображение ошибки Неверный код при авторизации по коду
    error_incorrect_code = WebElement(
        xpath='//span[@id="form-error-message" and contains(text(), "Неверный код. Повторите попытку")]')

    # Форма регистарции
    form_registration = WebElement(xpath='//div[@class="card-container__wrapper" and contains(text(), "Регистрация")]')

    # Ввод имени
    firstname_registration = WebElement(xpath='//input[@name="firstName"]')

    # Ввод фамилии
    lastname_registration = WebElement(xpath='//input[@name="lastName"]')

    # Ввод пароля на регистрации
    password_registration = WebElement(id='password')

    # Кнопка Зарегистрироваться
    registration_btn = WebElement(xpath='//button[@name="register" and @type="submit"]')

    # Приветствие
    welcome_text = WebElement(
        xpath='//div[@class="rtk-info-panel_wrapper"]/h2[contains(text(), "Добро пожаловать в Личный кабинет")]')

    # Кнопка войти в кабинет
    enter_btn = WebElement(xpath='//div[@class="btn-container"]/a[contains(text(), "Войти в кабинет")]')

    # Форма Учетная запись уже существует
    user_exist = WebElement(
        xpath='//div[@class="card-modal__card"]/h2[contains(text(), "Учётная запись уже существует")]')
