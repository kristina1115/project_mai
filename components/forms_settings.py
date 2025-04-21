from marina.common import wait
from marina.locators import form_audiences_settings_loc
from marina.components import question_icon
from selenium.webdriver.common.by import By
from marina.config import (audience_name, audience_changed_name, other_audience_name, indicator_1, indicator_2,
                           indicator_3, indicator_4)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


def click_button_add(driver, form_name):
    """Клик по кнопке добавления аудитории/канала/тематики и ожидание отображения заголовка соответствующей формы."""
    """Используем общий локатор кнопки для 3 подразделов вкладки "Настройки"."""
    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.BUTTON_ADD,
        "Кнопка 'Добавить...' не кликабельна."
    ).click()

    wait.presence(
        driver,
        (By.XPATH, "//span[text()='"+form_name+"']"),
        "Не найден заголовок формы."
    )


def add_indicators(driver):
    """Добавление в форму создания аудитории позитивного и негативного индикаторов."""
    wait.presence(
        driver,
        form_audiences_settings_loc.INDICATOR_FIELD,
        "Поле 'Индикаторы оценки аудитории' не найдено."
    ).send_keys(indicator_1)

    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.BUTTON_GREEN,
        "Кнопка с зеленым плюсом не кликабельна."
    ).click()

    wait.presence(
        driver,
        (By.XPATH, "//div[contains(@class,'positive')]//span[text()='" + indicator_1 + "']"),
        "Отсутствует индикатор '" + indicator_1 + "'."
    )

    wait.presence(
        driver,
        form_audiences_settings_loc.INDICATOR_FIELD,
        "Поле 'Индикаторы оценки аудитории' не найдено."
    ).send_keys(indicator_2)

    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.BUTTON_RED,
        "Кнопка с красным плюсом не кликабельна."
    ).click()

    wait.presence(
        driver,
        (By.XPATH, "//div[contains(@class,'negative')]//span[text()='" + indicator_2 + "']"),
        "Отсутствует индикатор '" + indicator_2 + "'."
    )


def delete_indicators(driver):
    """Проверка возможности удаления добавленных позитивного и негативного индикаторов из формы создания аудитории."""
    add_indicators(driver)

    wait.presence(
        driver,
        form_audiences_settings_loc.DELETE_BUTTON_GREEN,
        "Отсутствует кнопка удаления зеленого индикатора."
    ).click()

    wait.invisibility(
        driver,
        (By.XPATH, "//div[contains(@class,'positive')]//span[text()='" + indicator_3 + "']"),
        f"После удаления отображается индикатор '" + indicator_3 + "'."
    )

    wait.presence(
        driver,
        form_audiences_settings_loc.DELETE_BUTTON_RED,
        "Отсутствует кнопка удаления красного индикатора."
    ).click()

    wait.invisibility(
        driver,
        (By.XPATH, "//div[contains(@class,'negative')]//span[text()='" + indicator_4 + "']"),
        f"После удаления отображается индикатор '" + indicator_4 + "'."
    )


def form_fill_required_fields(driver):
    """Заполнение обязательных полей в форме создания аудитории без ее сохранения."""
    wait.presence(
        driver,
        form_audiences_settings_loc.NAME_FIELD,
        "Поле 'Название' не найдено."
    ).send_keys(audience_name)

    add_indicators(driver)


def form_fill_required_fields_and_save(driver):
    """Заполнение обязательных полей в форме создания аудитории и ее сохранение."""
    wait.presence(
        driver,
        form_audiences_settings_loc.NAME_FIELD,
        "Поле 'Название' не найдено."
    ).send_keys(audience_name)

    add_indicators(driver)

    save_new_audience(driver)


def save_new_audience(driver):
    """Нажатие кнопки сохранения в форме создания аудитории и проверка наличия новой аудитории в таблице аудиторий."""
    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.BUTTON_SUBMIT,
        "Кнопка 'Сохранить' не кликабельна."
    ).click()

    wait.presence(
        driver,
        (By.LINK_TEXT, f"{audience_name}"),
        f"Не найдена аудитория с названием {audience_name} в таблице аудиторий."
    )


def cancel_audience_creation(driver):
    """Удаление созданной аудитории и проверка ее отсутствия в таблице."""
    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.BUTTON_CANCEL,
        "Кнопка 'Отмена' не кликабельна."
    ).click()

    wait.invisibility(
        driver,
        (By.LINK_TEXT, f"{audience_name}"),
        f"Аудитория с названием {audience_name}, создание которой было отменено, отображается в таблице."
    )


def check_invisibility_audience_in_topic(driver):
    """Проверка в подразделе 'Тематики' отсутствия определенной аудитории."""
    name = question_icon.check_sub_tab_with_name(driver, "Тематики")
    assert name == "Тематики", "Подраздел 'Тематики' не активен."

    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.TOPIC_ELEMENT,
        "Не найден элемент шестеренки в таблице тематик."
    ).click()

    wait.invisibility(
        driver,
        (By.XPATH, f"//span[@title='{audience_name}']"),
        f"Аудитория с названием {audience_name} отображается в окне шестеренки."
    )


def check_connection_audience_with_topic(driver, topic_name):
    """Проверка в подразделе 'Тематики' наличия определенной аудитории и возможности связать ее с определенной
    тематикой."""
    name = question_icon.check_sub_tab_with_name(driver, "Тематики")
    assert name == "Тематики", "Подраздел 'Тематики' не активен."

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
    wait.presence(
        driver,
        (By.XPATH, f"//span[@title='{audience_name}']"),
        f"Не найдена аудитория с названием {audience_name} в таблице тематик."
    )

    checkbox = wait.to_be_clickable(
        driver,
        (By.XPATH, f"//span[@title='{audience_name}']/parent::label/preceding-sibling::div/input"),
        f"Чек-бокс аудитории {audience_name} не кликабелен."
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
    assert audience_name == name, f"Аудитория {audience_name} отсутствует для тематики {topic_name}."


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


def delete_audience(driver):
    """Удаление созданной аудитории 'Жители Воронежа' из таблицы аудиторий."""
    delete_button = wait.presence(
        driver,
        (By.XPATH, f"//a[text()='{audience_name}']//following::button[contains(@class, 'deleteBtn')]"),
        f"Отсутствует кнопка удаления аудитории {audience_name}."
    )
    delete_button.click()

    """Подтвердить удаление кликом по кнопке 'Да'."""
    wait.presence(
        driver,
        form_audiences_settings_loc.DELETE_CONFIRMATION_BUTTON,
        "Отсутствует кнопка 'Да'."
    ).click()

    """Проверка, что аудитории 'Жители Воронежа' исчезла из таблицы аудиторий."""
    wait.invisibility(
        driver,
        (By.LINK_TEXT, f"{audience_name}"),
        f"Аудитория {audience_name} отображается после удаления."
    )


def change_required_fields(driver):
    """Находим нужную аудиторию и переходим в ее форму."""
    wait.presence(
        driver,
        (By.LINK_TEXT, f"{audience_name}"),
        f"Отсутствует аудитория с названием {audience_name}."
    ).click()

    """Изменяем название аудитории и сохраняем в переменную 'new_name'."""
    name_field = wait.presence(
        driver,
        form_audiences_settings_loc.NAME_FIELD,
        "Поле 'Название' не найдено."
    )
    name_field.clear()
    name_field.send_keys(audience_changed_name)
    new_name = name_field.get_attribute("value")

    """Удаляем зеленый индикатор из формы и проверяем, что он не отображается."""
    wait.presence(
        driver,
        form_audiences_settings_loc.DELETE_BUTTON_GREEN,
        "Отсутствует кнопка удаления зеленого индикатора."
    ).click()

    wait.invisibility(
        driver,
        (By.XPATH, "//div[contains(@class,'positive')]//span[text()='" + indicator_1 + "']"),
        f"После удаления отображается индикатор '" + indicator_1 + "'."
    )

    """Добавляем новый зеленый индикатор."""
    wait.presence(
        driver,
        form_audiences_settings_loc.INDICATOR_FIELD,
        "Поле 'Индикаторы оценки аудитории' не найдено."
    ).send_keys(indicator_3)

    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.BUTTON_GREEN,
        "Кнопка с зеленым плюсом не кликабельна."
    ).click()

    wait.presence(
        driver,
        (By.XPATH, "//div[contains(@class,'positive')]//span[text()='" + indicator_3 + "']"),
        "Отсутствует индикатор '" + indicator_3 + "'."
    )

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
    ).send_keys(audience_changed_name)

    wait.invisibility(
        driver,
        (By.LINK_TEXT, f"{other_audience_name}"),
        f"Аудитория {other_audience_name} отображается после поиска аудитории {audience_changed_name}."
    )

    """Сохраняем измененное название аудитории в переменную 'name_audience_in_table'."""
    audience_in_table = wait.presence(
        driver,
        (By.LINK_TEXT, f"{audience_changed_name}"),
        f"Аудитория с названием {audience_changed_name} отсутствует."
    )
    name_audience_in_table = audience_in_table.text

    """Находим в таблице аудиторий столбец с названиями выбранных индикаторов."""
    indicators_in_table = wait.elements_presence(
        driver,
        form_audiences_settings_loc.INDICATOR_COLUMN,
        "Отсутствует список индикаторов в таблице аудиторий."
    )

    """Получаем список индикаторов из таблицы аудиторий и удаляем лишние запятые и пробелы."""
    new_indicators_list_in_table = [
        item.text.strip().rstrip(',')
        for item in indicators_in_table
        if item.text.strip().strip(',')
    ]
    """Сохраняем названия индикаторов в переменную 'new_indicators_in_table'."""
    new_indicators_in_table = ", ".join(new_indicators_list_in_table)

    return name_audience_in_table, new_name, new_indicators_in_table, new_indicators_names
