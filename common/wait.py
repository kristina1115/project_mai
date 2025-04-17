from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for(driver, condition, timeout=10, poll_frequency=1, timeout_message=None):
    """Универсальный метод ожидания."""
    return WebDriverWait(driver, timeout, poll_frequency).until(condition, message=timeout_message)


def presence(driver, selector, message):
    """Метод ожидает появления элемента в DOM."""
    timeout_message = f"{message} (проверка элемента: {selector})"
    return wait_for(driver, EC.presence_of_element_located(selector), timeout_message=timeout_message)


def elements_presence(driver, selector, message):
    """Метод ожидает появления списка элементов в DOM."""
    timeout_message = f"{message} (проверка элемента: {selector})"
    return wait_for(driver, EC.presence_of_all_elements_located(selector), timeout_message=timeout_message)


def to_be_clickable(driver, selector, message):
    """Метод ожидает пока элемент станет кликабельным."""
    timeout_message = f"{message} (проверка элемента: {selector})"
    return wait_for(driver, EC.element_to_be_clickable(selector), timeout_message=timeout_message)


def text_presence(driver, selector, text, message):
    """Метод ожидает появления нужного текста внутри элемента."""
    timeout_message = f"{message} (проверка элемента: {selector})"
    return wait_for(driver, EC.text_to_be_present_in_element(selector, text), timeout_message=timeout_message)


def visibility(driver, selector, message):
    """Метод принимает уже найденный WebElement и проверяет только его видимость (отображается ли он на странице)."""
    timeout_message = f"{message} (проверка элемента: {selector})"
    return wait_for(driver, EC.visibility_of(selector), timeout_message=timeout_message)


def elements_visibility(driver, selector, message):
    """Метод принимает уже найденный WebElement и проверяет только его видимость (отображается ли он на странице)."""
    timeout_message = f"{message} (проверка элемента: {selector})"
    return wait_for(driver, EC.visibility_of_all_elements_located(selector), timeout_message=timeout_message)


def invisibility(driver, selector, message):
    """Метод возвращает True, если элемент не найден в DOM или имеет display: none или visibility: hidden"""
    timeout_message = f"{message} (проверка элемента: {selector})"
    return wait_for(driver, EC.invisibility_of_element(selector), timeout_message=timeout_message)


def text_in_attribute(driver, selector, attribute, text, message):
    return wait_for(driver,
                    EC.text_to_be_present_in_element_attribute(selector, attribute, text),
                    timeout_message=message)
