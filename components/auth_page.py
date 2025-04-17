from marina.common import wait
from marina.locators import auth_locators
from marina.config import login, password


def execute_authorization(driver):
    """Метод для выполнения авторизации."""

    """Ожидаем поле для ввода email и передаем значение"""
    email_field = wait.presence(driver, auth_locators.INPUT_EMAIL, "Поле email не найдено.")
    email_field.send_keys(login)

    """Ожидаем поле для ввода пароля и передаем значение"""
    password_field = wait.presence(driver, auth_locators.INPUT_PASSWORD, "Поле password не найдено.")
    password_field.send_keys(password)

    """Ожидаем кликабельности кнопки "Вход" и выполняем клик"""
    button = wait.to_be_clickable(driver, auth_locators.BUTTON_SUBMIT, "Кнопка не кликабельна.")
    button.click()

    """Ожидаем появление заголовка с названием 'Картина дня за'."""
    wait.text_presence(driver,
                       auth_locators.PAGE_NAME,
                       "Картина дня за",
                       "Название страницы не соответствует 'Картина дня за'.")
