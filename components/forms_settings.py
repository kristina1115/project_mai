from marina.common import wait
from marina.locators import form_audiences_settings_loc
from marina.components import auth_page, question_icon
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
import random


def open_create_form(driver, tab_name, sub_tab_name, form_name):
    """
    1. Управляющий метод выполняет: авторизацию, переходит на заданную вкладку и подраздел, а затем открывает форму
    создания аудитории.

    :param driver: Экземпляр веб-драйвера Selenium.
    :param tab_name: Название вкладки (например, "Настройки").
    :param sub_tab_name: Название подраздела (например, "Аудитории").
    :param form_name: Название формы, которую ожидается открыть (например, "Аудитория").
    """
    # Авторизация
    auth_page.execute_authorization(driver)

    # Открытие вкладки "Настройки"
    active_tab_name = question_icon.check_active_tab_after_click(driver, tab_name)
    assert active_tab_name == "Настройки", "Название вкладки не соответствует 'Настройки'."

    # Открытие подраздела "Аудитории"
    name = question_icon.check_sub_tab_with_name(driver, sub_tab_name)
    assert name == "Аудитории", "Подраздел 'Аудитории' не активен."

    # Открытие формы создания аудитории
    click_button_add(driver, form_name)


def audience_form_fill(driver, name_audience, indicators, save):
    """
    2. Управляющий метод выполняет: заполнение поля "Название"; добавление индикаторов; нажатие кнопок в поле
    "Политическая ориентация", если параметр orientation=True; сохранение формы, если save=True и отмену создания
    аудитории, если save!=True.

    :param driver: Экземпляр веб-драйвера Selenium.
    :param name_audience: Название аудитории (например, "Жители Воронежа").
    :param indicators: Название параметров (например, "Архитектура, Набережная").
    :param save: Флаг, определяющий нажатие кнопок "Сохранить" (save=True) и "Отмена" (save!=True).
    """
    # Заполнение обязательного поля "Название"
    fill_name_audience_field(driver, name_audience)

    # Добавление индикаторов
    add_indicators(driver, indicators)

    if save is True:
        # Сохранение и проверка наличия аудитории в таблице аудиторий
        save_new_audience(driver, name_audience)

    else:
        # Отмена создания аудитории и проверка отсутствия аудитории в таблице аудиторий
        cancel_audience_creation(driver, name_audience)


def click_button_add(driver, form_name):
    """Клик по кнопке добавления аудитории/канала/тематики и ожидание отображения в форме заголовка (form_name)."""

    # Используем общий локатор кнопки для 3 подразделов вкладки "Настройки".
    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.BUTTON_ADD,
        "Кнопка 'Добавить...' не кликабельна."
    ).click()

    # Проверка соответствия заголовка формы.
    assert wait.presence(driver, (By.XPATH, "//span[text()='"+form_name+"']"), "Не найден заголовок формы.")


def fill_name_audience_field(driver, name_audience):
    name_audience_field = wait.presence(
            driver,
            form_audiences_settings_loc.NAME_FIELD,
            "Поле 'Название' не найдено."
        )
    name_audience_field.send_keys(name_audience)

    assert name_audience_field.get_attribute("value") == name_audience, \
        f"Значение в поле 'Название' не соответствует '{name_audience}'"


def add_indicators(driver, indicators):
    """Добавление в форму создания аудитории позитивного и негативного индикаторов."""
    for index, indicator in enumerate(indicators):
        indicator_field = wait.presence(
            driver,
            form_audiences_settings_loc.INDICATOR_FIELD,
            "Поле 'Индикаторы оценки аудитории' не найдено."
        )

        indicator_field.send_keys(indicator)

        assert indicator_field.get_attribute("value") == indicator, \
            f"Значение в поле 'Индикаторы оценки аудитории' не соответствует '{indicator}'"

        if index == 0:
            button_choice = "green"
        elif index == 1:
            button_choice = "red"
        else:
            # Случайный выбор красной и зеленой кнопок для третьего и далее индикаторов
            button_choice = random.choice(["green", "red"])

        if button_choice == "green":
            wait.to_be_clickable(
                driver,
                form_audiences_settings_loc.BUTTON_GREEN,
                "Кнопка с зеленым плюсом не кликабельна."
            ).click()

            assert wait.presence(
                driver,
                (By.XPATH, "//div[contains(@class,'positive')]//span[text()='" + indicator + "']"),
                "Отсутствует индикатор '" + indicator + "' в зеленом блоке."
            )
        else: # red
            wait.to_be_clickable(
                driver,
                form_audiences_settings_loc.BUTTON_RED,
                "Кнопка с красным плюсом не кликабельна."
            ).click()

            assert wait.presence(
                driver,
                (By.XPATH, "//div[contains(@class,'negative')]//span[text()='" + indicator + "']"),
                "Отсутствует индикатор '" + indicator + "' в красном блоке."
            )


def delete_indicators(driver, green, red):
    """Проверка возможности удаления позитивного и негативного индикаторов из формы создания аудитории."""
    if green:
        name_green = wait.presence(
            driver,
            form_audiences_settings_loc.NAME_INDICATOR_GREEN,
            "Отсутствует индикатор в зеленом блоке."
        ).text

        wait.to_be_clickable(
            driver,
            (By.XPATH, "//span[text()='"+name_green+"']/following-sibling::button"),
            "Кнопка удаления зеленого индикатора не кликабельна."
        ).click()

        assert wait.invisibility(
            driver,
            (By.XPATH, "//div[contains(@class,'positive')]//span[text()='" + name_green + "']"),
            f"После удаления отображается индикатор '" + name_green + "'."
        )
    if red:
        name_red = wait.presence(
            driver,
            form_audiences_settings_loc.NAME_INDICATOR_RED,
            "Отсутствует индикатор в красном блоке."
        ).text

        wait.to_be_clickable(
            driver,
            (By.XPATH, "//span[text()='" + name_red + "']/following-sibling::button"),
            "Отсутствует кнопка удаления красного индикатора."
        ).click()

        assert wait.invisibility(
            driver,
            (By.XPATH, "//div[contains(@class,'negative')]//span[text()='" + name_red + "']"),
            f"После удаления отображается индикатор '" + name_red + "'."
        )


def choice_orientation(driver, **kwargs):
    """Нажатие кнопок в поле 'Политическая ориентация', указанных в тест-кейсе."""
    orientation_elements = wait.elements_presence(
        driver,
        form_audiences_settings_loc.ORIENTATION,
        "Отсутствуют элементы в поле 'Политическая ориентация'."
    )

    for index, element in enumerate(orientation_elements):
        for value in kwargs.values():
            if element.text == value:
                element.click()


def save_new_audience(driver, name_audience):
    """Нажатие кнопки сохранения в форме создания аудитории и проверка наличия новой аудитории в таблице аудиторий."""
    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.BUTTON_SUBMIT,
        "Кнопка 'Сохранить' не кликабельна."
    ).click()

    assert wait.presence(
        driver,
        (By.LINK_TEXT, f"{name_audience}"),
        f"Не найдена аудитория с названием {name_audience} в таблице аудиторий."
    )


def check_connection_audience_with_topic(driver, name_audience, topic_name, sub_tab_name):
    """Проверка в подразделе 'Тематики' наличия определенной аудитории и возможности связать ее с определенной
    тематикой."""
    name = question_icon.check_sub_tab_with_name(driver, sub_tab_name)
    assert name == sub_tab_name, f"Подраздел '{sub_tab_name}' не активен."

    """Находим список тематик на странице и получаем индекс интересующей тематики 'Юбилей Воронежской губернии'."""
    topics = wait.elements_presence(driver, form_audiences_settings_loc.ROW_TOPIC, "Не найден список тем.")
    index = []
    for topic in topics:
        if topic_name in topic.text:
            index.append(topics.index(topic) + 1)
            break

    """Находим шестеренку, соответствующую тематике 'Юбилей Воронежской губернии' и кликаем."""
    wait.to_be_clickable(
        driver,
        (By.XPATH, f"(//button[contains(@class, 'Position')]){index}"),
        "Не найден элемент шестеренки в таблице тематик."
    ).click()

    """Находим в окне шестеренки название созданной аудитории и отмечаем чек-бокс возле нее."""
    assert wait.presence(
        driver,
        (By.XPATH, f"//span[@title='{name_audience}']"),
        f"Не найдена аудитория с названием {name_audience} в таблице тематик."
    )

    checkbox = wait.to_be_clickable(
        driver,
        (By.XPATH, f"//span[@title='{name_audience}']/parent::label/preceding-sibling::div/input"),
        f"Чек-бокс аудитории {name_audience} не кликабелен."
    )
    if checkbox.is_selected() is False:
        checkbox.click()

    """Выходим из окна шестеренки через клавишу ESC."""
    action = ActionChains(driver)
    action.send_keys(Keys.ESCAPE).perform()

    """Находим в столбце аудиторий поле, соответствующее выбранной тематике, и проверяем, что в нем отображается 
    добавленная аудитория."""
    topic_field = wait.elements_presence(
        driver,
        (By.XPATH, f"(//div[contains(@class, 'Audience')]){index}/span"),
        f"Не найдено поле аудиторий для тематики {topic_name}."
    )

    name = ", ".join(el.text for el in topic_field)
    assert name_audience == name, f"Аудитория {name_audience} отсутствует для тематики {topic_name}."


def cancel_audience_creation(driver, name_audience):
    """Удаление созданной аудитории и проверка ее отсутствия в таблице."""
    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.BUTTON_CANCEL,
        "Кнопка 'Отмена' не кликабельна."
    ).click()

    assert wait.invisibility(
        driver,
        (By.LINK_TEXT, f"{name_audience}"),
        f"Аудитория с названием {name_audience}, создание которой было отменено, отображается в таблице."
    )


def check_invisibility_audience_in_topic(driver, name_audience, sub_tab_name):
    """Проверка в подразделе 'Тематики' отсутствия определенной аудитории."""
    name = question_icon.check_sub_tab_with_name(driver, sub_tab_name)
    assert name == sub_tab_name, f"Подраздел '{sub_tab_name}' не активен."

    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.TOPIC_ELEMENT,
        "Не найден элемент шестеренки в таблице тематик."
    ).click()

    assert wait.invisibility(
        driver,
        (By.XPATH, f"//span[@title='{name_audience}']"),
        f"Аудитория с названием {name_audience} отображается в окне шестеренки."
    )


def delete_audience(driver, name_audience):
    """Удаление созданной аудитории "name_audience" из таблицы аудиторий."""
    wait.presence(
        driver,
        (By.XPATH, f"//a[text()='{name_audience}']//following::button[contains(@class, 'deleteBtn')]"),
        f"Отсутствует кнопка удаления аудитории {name_audience}."
    ).click()

    """Подтвердить удаление кликом по кнопке 'Да'."""
    wait.presence(
        driver,
        form_audiences_settings_loc.DELETE_CONFIRMATION_BUTTON,
        "Отсутствует кнопка 'Да'."
    ).click()

    """Проверка, что аудитории 'Жители Воронежа' не отображается в таблице аудиторий."""
    assert wait.invisibility(
        driver,
        (By.LINK_TEXT, f"{name_audience}"),
        f"Аудитория {name_audience} отображается после удаления."
    )


def change_required_fields(driver, name_audience, changed_name, other_audience_name, indicators, green, red):
    """Находим нужную аудиторию и переходим в ее форму."""
    wait.presence(
        driver,
        (By.LINK_TEXT, f"{name_audience}"),
        f"Отсутствует аудитория с названием {name_audience}."
    ).click()

    """Изменяем название аудитории и сохраняем в переменную 'new_name'."""
    name_field = wait.presence(
        driver,
        form_audiences_settings_loc.NAME_FIELD,
        "Поле 'Название' не найдено."
    )
    name_field.clear()
    name_field.send_keys(changed_name)
    new_name = name_field.get_attribute("value")

    """Удаляем зеленый индикатор из формы и проверяем, что он не отображается."""
    delete_indicators(driver, green, red)

    """Добавляем новый индикатор и проверяем, что он отображается."""
    add_indicators(driver, indicators)

    """Сохраняем названия индикаторов после изменения в переменную 'new_indicators_names'."""
    indicators = wait.elements_presence(
        driver,
        form_audiences_settings_loc.INDICATORS_BLOCKS,
        "Отсутствуют выбранные индикаторы."
    )
    new_indicators_names = ", ".join(indicator.text for indicator in indicators)

    """Сохраняем форму."""
    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.BUTTON_SUBMIT,
        "Кнопка 'Сохранить' не кликабельна."
    ).click()

    """Проверяем через поиск на странице аудиторий наличие измененного названия аудитории."""
    wait.presence(
        driver,
        form_audiences_settings_loc.SEARCH_FIELD,
        "Поле поиска отсутствует в подразделе аудиторий."
    ).send_keys(changed_name)

    wait.invisibility(
        driver,
        (By.LINK_TEXT, f"{other_audience_name}"),
        f"Аудитория {other_audience_name} отображается после поиска аудитории {changed_name}."
    )

    """Сохраняем измененное название аудитории в переменную 'name_audience_in_table'."""
    audience_in_table = wait.presence(
        driver,
        (By.LINK_TEXT, f"{changed_name}"),
        f"Аудитория с названием {changed_name} отсутствует."
    )
    name_audience_in_table = audience_in_table.text

    """Находим в таблице аудиторий столбец с названиями выбранных индикаторов."""
    indicators_in_table = wait.elements_presence(
        driver,
        form_audiences_settings_loc.INDICATOR_COLUMN,
        "Отсутствует список индикаторов в таблице аудиторий."
    )

    """Получаем названия индикаторов в виде списка и удаляем лишние запятые и пробелы."""
    new_indicators_list_in_table = [
        item.text.strip().rstrip(',')
        for item in indicators_in_table
        if item.text.strip().strip(',')
    ]
    """Полученные названия индикаторов преобразуем в строку и сохраняем в переменную 'new_indicators_in_table'."""
    new_indicators_in_table = ", ".join(new_indicators_list_in_table)

    return name_audience_in_table, new_name, new_indicators_in_table, new_indicators_names
