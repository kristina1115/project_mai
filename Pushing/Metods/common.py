from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from fixture import conftest


def wait_element(driver, locator, timeout=10, condition="visible"):
    """Универсальный метод ожидания элемента
    :param condition: "visible" | "clickable" | "present" | "invisible" | "allvisible"
    """
    conditions = {
        "visible": EC.visibility_of_element_located,          # Элемент виден
        "clickable": EC.element_to_be_clickable,              # Элемент кликабелен
        "present": EC.presence_of_element_located,            # Элемент есть в DOM
        "invisible": EC.invisibility_of_element_located,      # Элемент не виден
        "all_visible": EC.visibility_of_all_elements_located  # Все элементы видны
    }

    if condition not in conditions:
        raise ValueError(f"Неверный тип ожидания. Допустимо: {list(conditions.keys())}")

    try:
        return WebDriverWait(driver, timeout).until(
            conditions[condition](locator)
        )
    except TimeoutException:
        raise TimeoutException(f"Элемент {locator} не стал {condition} за {timeout} сек")


# Примеры использования:
# wait_element(driver, LOGIN_BUTTON, condition="clickable")
# wait_element(driver, PICTURE_DAY, condition="visible")


def check_site(driver):  #принимает драйвер и проверяет корректность сайта
    expected_title = "Ao24 | Главная"
    driver.get(conftest.url)
    WebDriverWait(driver, 10).until(
        EC.title_is(expected_title)
    )
    print("Проверка сайта: успешно")
    return True

