from marina.common import wait
from marina.locators import question_icon_loc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


def check_active_tab_name(driver):
    """Ожидаем появления активной вкладки и возвращаем ее название."""
    tab = wait.presence(driver, question_icon_loc.ACTIVE_TAB, "Активная вкладка отсутствует.")
    return tab.text


def check_active_tab_after_click(driver, name):
    """Клик по указанной вкладке."""
    wait.to_be_clickable(
        driver,
        (By.XPATH, "//span[text()='"+name+"']"),
        "Вкладка '"+name+"' не кликабельна."
    ).click()

    """Проверяем загрузку страницы наличием подраздела 'Аудитории', общего для вкладок 'Отчет' и 'Настройки'."""
    wait.presence(driver, question_icon_loc.BUTTON_REPORT, "Подраздел 'Аудитории' отсутствует на вкладке '"+name+"'.")

    """Найти активную вкладку и вернуть ее название."""
    tab = check_active_tab_name(driver)
    return tab


def check_click_question_icon(driver):
    """Переход в режим просмотра подсказок."""

    """Клик по иконке вопроса."""
    wait.to_be_clickable(driver, question_icon_loc.ICON, "Иконка с вопросом не кликабельна.").click()
    """Ожидание появления режима подсказок."""
    wait.presence(driver, question_icon_loc.HINT_MODE, "Режим подсказок не активен.")


def check_hints_with_and_without_pagination(driver):
    """Проверка отображения подсказок при наличии и отсутствии пагинации."""

    """Находим список элементов пагинации."""
    pagination = driver.find_elements(*question_icon_loc.PAGINATION_ELEMS)

    if len(pagination) > 1:

        """Если элементов пагинации больше 1, проверяем их переключение и отображение подсказок."""
        for index, i_pagination in enumerate(pagination):

            """Если элемент пагинации не активный, кликаем по нему и проверяем отображение подсказок."""
            if "active" not in i_pagination.get_attribute('class'):
                """Прокрутка вниз на 60 пикселей, иначе подсказка перекрывает элемент пагинации и он не кликается."""
                driver.execute_script("window.scrollBy(0, 60);")
                wait.to_be_clickable(driver, i_pagination,
                                     f"{index + 1}-й элемент пагинации не кликабелен.").click()
                driver.execute_script("window.scrollBy(0, -60);")
                """Проверка отображения подсказок."""
                check_hints_visibility(driver, index + 1)
            else:
                """Если элемент пагинации активный, то сразу проверяем отображение подсказок."""
                check_hints_visibility(driver, index + 1)
    else:
        """Если элементов пагинации нет, то сразу проверяем отображение подсказок."""
        check_hints_visibility(driver)


def check_hints_visibility(driver, position=1):
    """Проверка отображения подсказок при наличии и отсутствии контента, помеченного атрибутом 'data-onboarding'."""
    """Поиск элементов, помеченных атрибутом 'data-onboarding'."""
    data = driver.find_elements(*question_icon_loc.DATA)

    if len(data) < 1:
        """При отсутствии элементов, помеченных атрибутом 'data-onboarding' проверяем, что подсказки не отображаются."""
        wait.invisibility(
            driver,
            question_icon_loc.HELP_TEXT,
            f"Подсказки отображаются на {position}-м элементе при отсутствии контента с атрибутом 'data-onboarding'."
        )
    else:
        """Если элементов, помеченных атрибутом 'data-onboarding' больше нуля, проверяем отображение подсказок."""
        wait.elements_visibility(
            driver,
            question_icon_loc.HELP_TEXT,
            f"Подсказки не отображаются на {position}-м элементе."
        )


def exit_hints_mode(driver):
    """Выход из режима просмотра подсказок через нажатие клавиши ESC."""
    action = ActionChains(driver)
    action.send_keys(Keys.ESCAPE).perform()

    """Ожидание исчезновения режима подсказок."""
    return wait.invisibility(driver, question_icon_loc.HINT_MODE, "Режим подсказок активен.")


def check_sub_tab_without_name(driver, number):
    """Проверка активного статуса у подразделов без имени, расположенных на вкладке 'Картина дня'."""
    sub_tab = wait.presence(
        driver,
        (By.XPATH, f"//button[contains(@class, 'option')][{number}]"),
        "Отсутствует подраздел."
    )

    if "active" not in sub_tab.get_attribute('class'):
        wait.to_be_clickable(driver, sub_tab, f"Подраздел {number} не кликабелен.").click()

        wait.text_in_attribute(
            driver,
            (By.XPATH, f"//button[contains(@class, 'option')][{number}]"),
            'class',
            'active',
            "Подраздел не активен после клика."
        )


def check_sub_tab_with_name(driver, title):
    """Проверка активного статуса у подразделов с именами, расположенных на вкладках 'Отчет' и 'Настройки'."""
    sub_tab = wait.presence(
        driver,
        (By.XPATH, "//button[text()='"+title+"']"),
        "Отсутствует подраздел."
    )

    if "active" not in sub_tab.get_attribute('class'):
        wait.to_be_clickable(driver, sub_tab, f"Подраздел {sub_tab.text} не кликабелен.").click()

        wait.text_in_attribute(
            driver,
            (By.XPATH, "//button[text()='"+title+"']"),
            'class',
            'active',
            "Подраздел не активен после клика."
        )
    return sub_tab.text


def check_hints_without_pagination(driver):
    """Клик по иконке с вопросом."""
    check_click_question_icon(driver)

    """Проверяем отображение подсказок при наличии контента."""
    check_hints_visibility(driver)

    """Выход из режима просмотра подсказок."""
    return exit_hints_mode(driver)
