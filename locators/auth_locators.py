from selenium.webdriver.common.by import By

"""Найдет соответствующие поля и кнопки на Authorization & Registration page"""
INPUT_EMAIL = (By.XPATH, "//input[@name='email']")
INPUT_PASSWORD = (By.XPATH, "//input[@name='password']")
BUTTON_SUBMIT = (By.XPATH, "//button[@type='submit']")

"""Main page: можно найти заголовок на странице авторизации - "Вход", регистрации - "Регистрация", на стартовой странице
 на вкладке "Картина дня" - заголовок "Картина дня за" и на вкладке "Настройки" - заголовок "Настройки мониторинга"."""
PAGE_NAME = (By.XPATH, "//span[contains(@class, 'Title_Title')]")
