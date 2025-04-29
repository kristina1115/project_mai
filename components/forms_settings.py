from marina.common import wait
from marina.locators import form_audiences_settings_loc, form_channels_loc
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
    assert name == f"{sub_tab_name}", f"Подраздел '{sub_tab_name}' не активен."

    # Открытие формы создания аудитории
    click_button_add(driver, form_name)


def audience_form_fill(driver, name_audience, sub_tab_name, indicators, save):
    """
    2. Управляющий метод выполняет: заполнение поля "Название"; добавление индикаторов; сохранение формы, если
        save=True и отмену создания аудитории, если save!=True.

    :param driver: Экземпляр веб-драйвера Selenium.
    :param name_audience: Название аудитории (например, "Жители Воронежа").
    :param sub_tab_name: Название подраздела (например, "Аудитории").
    :param indicators: Название параметров (например, "Архитектура, Набережная").
    :param save: Флаг, определяющий нажатие кнопок "Сохранить" (save=True) и "Отмена" (save!=True).
    """
    # Заполнение обязательного поля "Название"
    fill_name_field(driver, name_audience)

    # Добавление индикаторов
    add_indicators(driver, indicators)

    if save is True:
        # Сохранение и проверка наличия аудитории в таблице аудиторий
        save_form(driver, name_audience, sub_tab_name)

    else:
        # Отмена создания аудитории и проверка отсутствия аудитории в таблице аудиторий
        cancel_form_creation(driver, name_audience, sub_tab_name)


def click_button_add(driver, form_name):
    """Клик по кнопке добавления аудитории/канала/тематики и ожидание отображения в форме заголовка (form_name)."""

    # Используем общий локатор кнопки для 3 подразделов вкладки "Настройки".
    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.BUTTON_ADD,
        "Кнопка 'Добавить...' не кликабельна."
    ).click()

    # Проверка соответствия заголовка формы.
    assert wait.presence(
        driver,
        (By.XPATH, "//span[text()='"+form_name+"']"),
        "Не найден заголовок формы."
    )


def fill_name_field(driver, name):
    name_field = wait.presence(
            driver,
            form_audiences_settings_loc.NAME_FIELD,
            "Поле 'Название' не найдено."
        )
    name_field.clear()
    name_field.send_keys(name)

    assert name_field.get_attribute("value") == name, \
        f"Значение в поле 'Название' не соответствует '{name}'"


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


def save_form(driver, name, sub_tab_name):
    """Сохранение формы и проверка ее наличия в таблице."""
    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.BUTTON_SUBMIT,
        "Кнопка 'Сохранить' не кликабельна."
    ).click()

    if sub_tab_name == "Аудитории":
        assert wait.presence(driver, (By.LINK_TEXT, f"{name}"), f"Аудитория {name} не сохранилась.")
    elif sub_tab_name == "Каналы":
        assert wait.presence(driver, (By.XPATH, f"//span[text()='{name}']"), f"Канал {name} не сохранился.")


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


def cancel_form_creation(driver, name, sub_tab_name):
    """Отмена создания аудитории/канала/тематики и проверка ее отсутствия в таблице."""
    wait.to_be_clickable(
        driver,
        form_audiences_settings_loc.BUTTON_CANCEL,
        "Кнопка 'Отмена' не кликабельна."
    ).click()

    if sub_tab_name == "Аудитории":
        assert wait.invisibility(
            driver,
            (By.LINK_TEXT, f"{name}"),
            f"После отмены сохранения аудитория с названием {name} отображается в таблице."
        )

    elif sub_tab_name == "Каналы":
        assert wait.invisibility(
            driver,
            (By.XPATH, f"//span[text()='{name}']"),
            f"После отмены сохранения канал с названием {name} отображается в таблице."
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


def check_before_delete(driver, tab_name, sub_tab_name):
    # Проверить, что выбрана вкладка "Настройки"
    active_tab_name = question_icon.check_active_tab_after_click(driver, tab_name)
    assert active_tab_name == f"{tab_name}", f"Название вкладки не соответствует '{tab_name}'."

    # Проверка/переход на подраздел "sub_tab_name"
    active_subtab_name = question_icon.check_sub_tab_with_name(driver, sub_tab_name)
    assert active_subtab_name == f"{sub_tab_name}", f"Подраздел '{sub_tab_name}' не активен."

    # Проверка/ожидание загрузки таблицы в выбранном подразделе (привязываемся к появлению названия заголовка первого
    # столбца в таблице)
    locators_title_column = {
        "Аудитории": (form_audiences_settings_loc.AUDIENCE_TITLE_COLUMN, "Таблица аудиторий отсутствует."),
        "Каналы": (form_channels_loc.CHANNEL_TITLE_COLUMN, "Таблица каналов отсутствует."),
        "Тематики": (form_audiences_settings_loc.TOPIC_TITLE_COLUMN, "Таблица тематик отсутствует.")
    }
    locator, timeout_message = locators_title_column[sub_tab_name]
    wait.presence(driver, locator, timeout_message)

    # Получение списка названий аудиторий/ каналов/ тематик
    locators = {
        "Аудитории": (form_audiences_settings_loc.LINK_SUBSTANCE, "Список аудиторий отсутствует."),
        "Каналы": (form_channels_loc.ROW, "Список каналов отсутствует."),
        "Тематики": (form_audiences_settings_loc.TOPIC_NAME, "Список тематик отсутствует.")
    }

    locator, timeout_message = locators[sub_tab_name]
    rows_in_table = wait.elements_presence(driver, locator, timeout_message)
    names_rows = [row.text for row in rows_in_table]

    return names_rows


def delete_substance(driver, name_substance, sub_tab_name):
    """Удаление созданной сущности "name_substance" из таблицы сущностей."""
    # Создание словаря локаторов для поиска списка сущностей, кнопок их удаления и конкретного названия сущности в трех
    # разных подразделах Аудитории/ Каналы/ Тематики
    locators = {
        "Аудитории": {
            "row_locator": form_audiences_settings_loc.LINK_SUBSTANCE,
            "delete_button_base": "//button[contains(@class, 'delete')]",
            "name_locator": (By.LINK_TEXT, name_substance)
        },
        "Каналы": {
            "row_locator": form_channels_loc.ROW,
            "delete_button_base": "//div[contains(@class, 'Trash')]",
            "name_locator": (By.XPATH, f"//span[text()='{name_substance}']")
        },
        "Тематики": {
            "row_locator": form_audiences_settings_loc.TOPIC_NAME,
            "delete_button_base": "//div[contains(@class, 'PositionBox')]",
            "name_locator": (By.XPATH, f"//span[text()='{name_substance}']")
        }
    }
    # Получение набора локаторов из словаря выше для конкретного подраздела Аудитории/ Каналы/ Тематики
    locator_set = locators.get(sub_tab_name)

    # Если значение sub_tab_name не соответствует Аудитории/ Каналы/ Тематики, выбросить ошибку
    if not locator_set:
        raise ValueError(f"Неизвестный подраздел: {sub_tab_name}")

    # Получение списка названий сущностей из таблицы в подразделе Аудитории/ Каналы/ Тематики
    rows = wait.elements_presence(driver, locator_set["row_locator"], "Список отсутствует.")
    names = [row.text for row in rows]

    # Определение порядкового номера "idx" нужного названия сущности либо возврат ошибки об отсутствии сущности
    try:
        idx = names.index(name_substance) + 1
    except ValueError:
        raise ValueError(f"Сущность '{name_substance}' не найдена в подразделе '{sub_tab_name}'.")

    # Клик по кнопке удаления сущности по найденному номеру "idx"
    delete_button_locator = (By.XPATH, f"({locator_set['delete_button_base']})[{idx}]")
    wait.to_be_clickable(driver, delete_button_locator, "Кнопка удаления не кликабельна.").click()
    wait.presence(
        driver,
        form_audiences_settings_loc.DELETE_CONFIRMATION_BUTTON,
        "Нет кнопки подтверждения удаления."
    ).click()

    # Ввод в поле поиска названия искомой сущности
    search_field = wait.presence(driver, form_audiences_settings_loc.SEARCH_FIELD, "Нет поля поиска.")
    search_field.clear()
    search_field.send_keys(name_substance)

    # Проверка отсутствия названия удаленной сущности в таблице аудиторий/ каналов/ тематик
    wait.invisibility(driver, locator_set["name_locator"], f"{name_substance} всё ещё видно после удаления.")


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
    search_field = wait.to_be_clickable(driver, form_audiences_settings_loc.SEARCH_FIELD, "Нет поля поиска.")
    search_field.clear()
    search_field.send_keys(changed_name)

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


"""------------------------------Специализированные методы для подраздела "Каналы".---------------------------------"""


def choice_in_select_field(driver, option_name):
    """Выбор из выпадающего списка указанного значения."""

    # Найти поле селекта и кликнуть
    select_input = wait.presence(driver, form_channels_loc.SELECT_FIELD, "Поле 'Тип' отсутствует.")
    select_input.click()

    # Кликнуть указанное значение "option_name" в выпадающем списке
    wait.to_be_clickable(
        driver,
        (By.XPATH, "//div[text()='"+option_name+"']"),
        f"Тип '{option_name}' не кликабелен."
    ).click()

    # Проверить, что в поле селекта отображается указанное значение "option_name"
    wait.text_in_attribute(
        driver,
        form_channels_loc.SELECT_FIELD,
        "value", f"{option_name}",
        f"В поле селекта отображается не {option_name}."
    )


def identifier_field(driver, address):
    identifier_input = wait.to_be_clickable(driver, form_channels_loc.IDENTIFIER_FIELD, "Поле не кликабельно.")
    identifier_input.clear()
    identifier_input.send_keys(f"{address}")
    assert identifier_input.get_attribute("value") == address, f"В поле значение не соответствует '{address}'."


def channel_form_fill(driver, name_channel, sub_tab_name, option_name, address, save):
    """
    3. Управляющий метод для создания канала выполняет: заполнение поля "Название"; добавление индикаторов; сохранение
        формы, если save=True и отмена создания, если save!=True.

    :param driver: Экземпляр веб-драйвера Selenium.
    :param name_channel: Название канала (например, "Афиша Воронежа").
    :param sub_tab_name: Название подраздела (например, "Каналы").
    :param option_name: Название типа канала ("Telegram" или "Внутренний").
    :param address: ссылка на канал (например, "https://t.me/afisha_voronezh/797").
    :param save: Флаг, определяющий нажатие кнопок "Сохранить" (save=True) и "Отмена" (save!=True).
    """
    # Заполнение обязательного поля "Название"
    fill_name_field(driver, name_channel)

    # Если выбран какой-то тип канала
    if option_name:
        choice_in_select_field(driver, option_name)

        # Если выбран тип канала НЕ "Внутренний" и введён идентификатор
        if option_name != "Внутренний" and address:
            identifier_field(driver, address)

    if save is True:
        # Сохранение и проверка наличия канала в таблице каналов
        save_form(driver, name_channel, sub_tab_name)

    else:
        # Отмена создания канала и проверка отсутствия канала в таблице каналов
        cancel_form_creation(driver, name_channel, sub_tab_name)


def change_form(driver, name_channel, form_name, new_name, option_name, address, save, sub_tab_name):
    """Редактирование формы текущего канала."""
    # Войти в форму указанного канала, кликнув по его названию в таблице
    wait.to_be_clickable(
        driver,
        (By.XPATH, f"//span[text()='{name_channel}']"),
        f"Канал '{name_channel}' не кликабелен.").click()

    # Проверить, что форма открылась и отображается ее заголовок (Изменить канал)
    assert wait.presence(
        driver,
        (By.XPATH, f"//span[text()='{form_name}']"),
        "Не найден заголовок формы."
    )

    # Если указано значение в параметре new_name (т.е. \'new_name'\ != None), то поле "Название" изменяется
    if new_name:
        fill_name_field(driver, new_name)

    # Если указано значение в параметре address (т.е. \'address'\ != None), то поле "Идентификатор" изменяется
    if address:
        identifier_field(driver, address)

    # Если указано значение в параметре option_name (т.е. \'option_name'\ != None), то поле "Тип" изменяется
    if option_name:
        choice_in_select_field(driver, option_name)

    if save is True and new_name:
        # Сохранение изменений и проверка измененного канала в таблице каналов
        save_form(driver, new_name, sub_tab_name)

    elif save is True and not new_name:
        # Сохранение изменений, не включающих изменение название канала, и проверка наличия канала в таблице каналов
        save_form(driver, name_channel, sub_tab_name)

    elif save is False:
        # Отмена изменений и проверка отсутствия измененного канала в таблице каналов
        cancel_form_creation(driver, new_name, sub_tab_name)
