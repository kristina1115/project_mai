from marina.components import forms_settings


def test_creation_audience_only_required_fields(driver):

    """1. Открыть форму создания аудитории."""
    forms_settings.open_create_form(driver, tab_name="Настройки", sub_tab_name="Аудитории", form_name="Аудитория")

    """2. Заполнить в форме только обязательные поля и сохранить."""
    forms_settings.audience_form_fill(
        driver,
        name_audience="Жители Воронежа",
        indicators=["Архитектура", "Набережная"],
        save=True
    )

    """
    3. Проверка в подразделе 'Тематики' наличия определенной аудитории и возможности связать ее с определенной
        тематикой.
    """
    forms_settings.check_connection_audience_with_topic(
        driver,
        name_audience="Жители Воронежа",
        sub_tab_name="Тематики",
        topic_name="Юбилей Воронежской губернии")


def test_creation_audience_all_fields_all_orientations(driver):

    """1. Открыть форму создания аудитории."""
    forms_settings.open_create_form(driver, tab_name="Настройки", sub_tab_name="Аудитории", form_name="Аудитория")

    """2. Нажать все кнопки в блоке 'Политическая ориентация'."""
    forms_settings.choice_orientation(
        driver,
        button1="Ультраконсерваторы",
        button2="Консерваторы",
        button3="Центристы",
        button4="Либералы",
        button5="Ультралибералы"
    )

    """3. Заполнить в форме обязательные поля и сохранить."""
    forms_settings.audience_form_fill(
        driver,
        name_audience="Жители Липецка",
        indicators=["Религия"],
        save=True
    )


def test_creation_audience_all_fields_one_orientation(driver):

    """1. Открыть форму создания аудитории."""
    forms_settings.open_create_form(driver, tab_name="Настройки", sub_tab_name="Аудитории", form_name="Аудитория")

    """2. Нажать одну кнопку в блоке 'Политическая ориентация'."""
    forms_settings.choice_orientation(
        driver,
        button3="Центристы"
    )

    """3. Заполнить в форме обязательные поля и сохранить."""
    forms_settings.audience_form_fill(
        driver,
        name_audience="Жители Ростова",
        indicators=["Рестораны", "Медицина", "Религия"],
        save=True
    )


def test_add_audience_cancel(driver):

    """1. Открыть форму создания аудитории."""
    forms_settings.open_create_form(driver, tab_name="Настройки", sub_tab_name="Аудитории", form_name="Аудитория")

    """2. Заполнить в форме обязательные поля и нажать кнопку "Отмена"."""
    forms_settings.audience_form_fill(
        driver,
        name_audience="Жители Челябинска",
        indicators=["Фабрики", "Торговля"],
        save=False
    )

    """3. Проверка в подразделе 'Тематики' отсутствия определенной аудитории."""
    forms_settings.check_invisibility_audience_in_topic(
        driver,
        name_audience="Жители Челябинска",
        sub_tab_name="Тематики"
    )


def test_delete_audience_from_table(driver):

    """1. Открыть форму создания аудитории."""
    forms_settings.open_create_form(driver, tab_name="Настройки", sub_tab_name="Аудитории", form_name="Аудитория")

    """2. Заполнить в форме только обязательные поля и сохранить."""
    forms_settings.audience_form_fill(
        driver,
        name_audience="Жители Калининграда",
        indicators=["Политика", "Транспорт", "Фабрики", "Торговля", "Рестораны"],
        save=True
    )

    """
    3. Удалить созданную аудиторию "name_audience" из таблицы аудиторий и проверить, что она не отображается в
        таблице аудиторий.
    """
    forms_settings.delete_audience(driver, name_audience="Жители Калининграда")

    """4. Проверить, что удаленная аудитория не отображается в подразделе "Тематики" в окне шестеренки."""
    forms_settings.check_invisibility_audience_in_topic(
        driver,
        name_audience="Жители Калининграда",
        sub_tab_name="Тематики"
    )


def test_add_audience_delete_indicator(driver):

    """1. Открыть форму создания аудитории."""
    forms_settings.open_create_form(driver, tab_name="Настройки", sub_tab_name="Аудитории", form_name="Аудитория")

    """2. Добавить индикаторы."""
    forms_settings.add_indicators(
        driver,
        indicators=["ЖКХ", "Страхование", "Строительство", "Образование"]
    )

    """3. Удалить указанные индикаторы."""
    forms_settings.delete_indicators(driver, green=True, red=True)


def test_update_audience_form(driver):

    """1. Открыть форму создания аудитории."""
    forms_settings.open_create_form(driver, tab_name="Настройки", sub_tab_name="Аудитории", form_name="Аудитория")

    """2. Заполнить в форме только обязательные поля и сохранить."""
    forms_settings.audience_form_fill(
        driver,
        name_audience="Жители Орла",
        indicators=["Политика", "Транспорт", "Фабрики"],
        save=True
    )

    """3. Отредактировать созданную аудиторию и проверить, что изменения сохранились."""
    (name_audience_in_table,
     new_name_in_form,
     new_indicators_in_table,
     new_indicators_names_in_form
     ) = forms_settings.change_required_fields(driver,
                                                name_audience="Жители Орла",
                                                changed_name="Россияне",
                                                other_audience_name="Москвичи",
                                                indicators=["Путешествия"],
                                                green=True,
                                                red=False
                                            )

    assert name_audience_in_table == new_name_in_form, \
        f"Название аудитории в таблице {name_audience_in_table} не соответствует названию в форме'{new_name_in_form}'."

    assert new_indicators_in_table == new_indicators_names_in_form, \
        f"Название индикаторов аудитории в таблице {new_indicators_in_table} не соответствует индикаторам в форме {new_indicators_names_in_form}."
