import pytest
import logging
from marina.components import forms_settings


@pytest.fixture()
def data_audience(driver, sub_tab_name_check="Аудитории"):
    # Список названий тестовых аудиторий
    audience_names = [
        "Жители Воронежа",
        "Жители Липецка",
        "Жители Ростова",
        "Россияне"
    ]
    # Открытие формы
    forms_settings.open_create_form(
        driver,
        tab_name="Настройки",
        sub_tab_name=sub_tab_name_check,
        form_name="Аудитория"
    )

    # Передаём список названий тестовых аудиторий в тест
    yield audience_names

    # Переход на нужный подраздел и получение текущего списка аудиторий
    names_audiences_in_table = forms_settings.check_before_delete(
        driver,
        tab_name="Настройки",
        sub_tab_name=sub_tab_name_check
    )

    # Проверка наличия тестовой аудитории в текущем списке аудиторий и ее удаление
    for name in audience_names:
        if name in names_audiences_in_table:
            forms_settings.delete_substance(driver, name_substance=name, sub_tab_name=sub_tab_name_check)
            logging.info("Тестовая аудитория удалена.")
            break


def test_creation_audience_only_required_fields(driver, data_audience):
    logging.info("Тест начинается...")

    """1. Заполнить в форме только обязательные поля и сохранить."""
    forms_settings.audience_form_fill(
        driver,
        name_audience="Жители Воронежа",
        sub_tab_name="Аудитории",
        indicators=["Архитектура", "Набережная"],
        save=True
    )

    """
    2. Проверка в подразделе 'Тематики' наличия определенной аудитории и возможности связать ее с определенной
        тематикой.
    """
    forms_settings.check_connection_audience_with_topic(
        driver,
        name_audience="Жители Воронежа",
        sub_tab_name="Тематики",
        topic_name="Юбилей Воронежской губернии")
    logging.info("Тест завершён.")


def test_creation_audience_all_fields_all_orientations(driver, data_audience):

    """1. Нажать все кнопки в блоке 'Политическая ориентация'."""
    forms_settings.choice_orientation(
        driver,
        button1="Ультраконсерваторы",
        button2="Консерваторы",
        button3="Центристы",
        button4="Либералы",
        button5="Ультралибералы"
    )

    """2. Заполнить в форме обязательные поля и сохранить."""
    forms_settings.audience_form_fill(
        driver,
        name_audience="Жители Липецка",
        sub_tab_name="Аудитории",
        indicators=["Религия"],
        save=True
    )


def test_creation_audience_all_fields_one_orientation(driver, data_audience):

    """1. Нажать одну кнопку в блоке 'Политическая ориентация'."""
    forms_settings.choice_orientation(
        driver,
        button3="Центристы"
    )

    """2. Заполнить в форме обязательные поля и сохранить."""
    forms_settings.audience_form_fill(
        driver,
        name_audience="Жители Ростова",
        sub_tab_name="Аудитории",
        indicators=["Рестораны", "Медицина", "Религия"],
        save=True
    )


def test_add_audience_cancel(driver, data_audience):

    """1. Заполнить в форме обязательные поля и нажать кнопку "Отмена"."""
    forms_settings.audience_form_fill(
        driver,
        name_audience="Жители Челябинска",
        sub_tab_name="Аудитории",
        indicators=["Фабрики", "Торговля"],
        save=False
    )

    """2. Проверка в подразделе 'Тематики' отсутствия определенной аудитории."""
    forms_settings.check_invisibility_audience_in_topic(
        driver,
        name_audience="Жители Челябинска",
        sub_tab_name="Тематики"
    )


def test_delete_audience_from_table(driver, data_audience):

    """1. Заполнить в форме только обязательные поля и сохранить."""
    forms_settings.audience_form_fill(
        driver,
        name_audience="Жители Калининграда",
        sub_tab_name="Аудитории",
        indicators=["Политика", "Транспорт", "Фабрики", "Торговля", "Рестораны"],
        save=True
    )

    """
    2. Удалить созданную аудиторию "name_audience" из таблицы аудиторий и проверить, что она не отображается в
        таблице аудиторий.
    """
    forms_settings.delete_substance(
        driver,
        name_substance="Жители Калининграда",
        sub_tab_name="Аудитории"
    )

    """3. Проверить, что удаленная аудитория не отображается в подразделе "Тематики" в окне шестеренки."""
    forms_settings.check_invisibility_audience_in_topic(
        driver,
        name_audience="Жители Калининграда",
        sub_tab_name="Тематики"
    )


def test_add_audience_delete_indicator(driver, data_audience):

    """1. Добавить индикаторы."""
    forms_settings.add_indicators(
        driver,
        indicators=["ЖКХ", "Страхование", "Строительство", "Образование"]
    )

    """2. Удалить указанные индикаторы."""
    forms_settings.delete_indicators(driver, green=True, red=True)


def test_update_audience_form(driver, data_audience):

    """1. Заполнить в форме только обязательные поля и сохранить."""
    forms_settings.audience_form_fill(
        driver,
        name_audience="Жители Орла",
        sub_tab_name="Аудитории",
        indicators=["Политика", "Транспорт", "Фабрики"],
        save=True
    )

    """2. Отредактировать созданную аудиторию и проверить, что изменения сохранились."""
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
        (f"Название индикаторов аудитории в таблице {new_indicators_in_table} не соответствует индикаторам "
         f"в форме {new_indicators_names_in_form}.")
