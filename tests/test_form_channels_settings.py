import pytest
import logging
from marina.components import forms_settings


@pytest.fixture()
def data_channels(driver, sub_tab_name_check="Каналы"):
    # Список ссылок на тестовые каналы
    channel_names = [
        "555",
        "Афиша Воронеж",
        "Типичный Воронеж",
        "111",
        "Новости",
        "Итоги",
        "Мой город"
    ]

    # Открытие формы
    forms_settings.open_create_form(
        driver,
        tab_name="Настройки",
        sub_tab_name=sub_tab_name_check,
        form_name="Добавьте канал"
    )

    # Передаём список названий в тест
    yield channel_names

    # Переход на нужный подраздел и получение текущего списка каналов
    names_channels_in_table = forms_settings.check_before_delete(
        driver,
        tab_name="Настройки",
        sub_tab_name=sub_tab_name_check
    )

    # Проверка наличия тестового канала в текущем списке каналов и его удаление
    for name in channel_names:
        if name in names_channels_in_table:
            forms_settings.delete_substance(driver, name_substance=name, sub_tab_name=sub_tab_name_check)
            logging.info("Удаление тестовых данных завершено.")
            break


def test_form_channels_only_name_field(driver, data_channels):
    """1. Проверка сохранения формы "Добавьте канал" с заполнением только обязательного поля "Название" и проверка
      наличия созданного канала в таблице каналов."""

    forms_settings.channel_form_fill(
        driver,
        name_channel="555",
        sub_tab_name="Каналы",
        option_name=None,
        address=None,
        save=True
    )


def test_form_channels_all_fields_type_telegram(driver, data_channels):
    """2. Проверка сохранения формы "Добавьте канал" с заполнением всех полей, включая выбор типа "Telegram" и
        заполнением поля "Идентификатор"."""

    # Заполнение полей формы и проверка наличия названия созданного канала в таблице каналов
    forms_settings.channel_form_fill(
        driver,
        name_channel="Афиша Воронеж",
        sub_tab_name="Каналы",
        option_name="Telegram",
        address="https://t.me/afisha_voronezh/797",
        save=True
    )

    # Проверка соответствия ссылки, введенной в поля "Идентификатор", ссылке в таблице каналов
    link_address = driver.find_element("xpath", "//span[text()='Афиша Воронеж']/following::a/span").text
    assert link_address == "https://t.me/afisha_voronezh/797", \
        "Ссылка канала 'Афиша Воронеж' не соответствует сохраненному идентификатору в форме."


def test_form_channels_fields_name_type_telegram_without_identifier(driver, data_channels):
    """3. Проверка сохранения формы "Добавьте канал" с заполнением полей "Название", выбором типа "Telegram", без
        заполнения поля "Идентификатор"."""

    forms_settings.channel_form_fill(
        driver,
        name_channel="Типичный Воронеж",
        sub_tab_name="Каналы",
        option_name="Telegram",
        address=None,
        save=True
    )


def test_form_channels_all_fields_type_inner(driver, data_channels):
    """4. Проверка сохранения формы "Добавьте канал" с заполнением названия и выбором типа "Внутренний"."""

    forms_settings.channel_form_fill(
        driver,
        name_channel="111",
        sub_tab_name="Каналы",
        option_name="Внутренний",
        address=None,
        save=True
    )


def test_cancel_form_with_type_inner(driver, data_channels):
    """5. Проверка отмены сохранения формы "Добавьте канал" с заполнением названия и выбором типа "Внутренний"."""

    forms_settings.channel_form_fill(
        driver,
        name_channel="112",
        sub_tab_name="Каналы",
        option_name="Внутренний",
        address=None,
        save=False
    )


def test_update_form_all_fields(driver, data_channels):
    """6. Проверка сохранения изменений (изменение названия, идентификатора и типа с Telegram на "Внутренний") в
        существующей форме."""

    # Заполнение полей формы и проверка наличия названия созданного канала в таблице каналов
    forms_settings.channel_form_fill(
        driver,
        name_channel="Афиша Воронеж",
        sub_tab_name="Каналы",
        option_name="Telegram",
        address="https://t.me/afisha_voronezh/797",
        save=True
    )

    # Открытие формы канала "Афиша Воронеж", редактирование указанных полей и проверка изменений в таблице каналов,
    # включая проверку нового названия канала в таблице
    forms_settings.change_form(
        driver,
        name_channel="Афиша Воронеж",
        form_name="Изменить канал",
        new_name="Новости",
        option_name="Внутренний",
        address="000",
        save=True,
        sub_tab_name="Каналы"
    )

    # Проверка, что старое название канала "Афиша Воронеж" отсутствует в таблице
    old_name = driver.find_elements("xpath", "//span[text()='Афиша Воронеж']")
    assert len(old_name) == 0, "Название канала 'Афиша Воронеж' продолжает отображаться в таблице."

    # Проверка соответствия ссылки, измененной в поле "Идентификатор", ссылке в таблице каналов
    link_address = driver.find_element("xpath", "//span[text()='Новости']/following::a/span").text
    assert link_address == "000", \
        "Ссылка канала 'Новости' не соответствует измененному идентификатору в форме."


def test_update_form_only_type_field(driver, data_channels):
    """7. Проверка сохранения изменений только для поля "Тип" (с Telegram на "Внутренний") в существующей форме."""

    # Заполнение полей формы и проверка наличия названия созданного канала в таблице каналов
    forms_settings.channel_form_fill(
        driver,
        name_channel="Итоги",
        sub_tab_name="Каналы",
        option_name="Telegram",
        address="https://t.me/afisha_voronezh/797",
        save=True
    )

    # Открытие формы канала "Итоги", редактирование указанных полей и проверка изменений в таблице каналов
    forms_settings.change_form(
        driver,
        name_channel="Итоги",
        form_name="Изменить канал",
        new_name=None,
        option_name="Внутренний",
        address=None,
        save=True,
        sub_tab_name="Каналы"
    )

    # Проверка соответствия ссылки, не измененной в поле "Идентификатор", ссылке в таблице каналов
    link_address = driver.find_element("xpath", "//span[text()='Итоги']/following::a/span").text
    assert link_address == "https://t.me/afisha_voronezh/797", \
        "Ссылка канала 'Итоги' не соответствует измененному идентификатору в форме."


def test_cancel_update_form_only_identifier(driver, data_channels):
    """8. Проверка отмены сделанных изменений в форме только для поля "Идентификатор"."""

    # Заполнение полей формы и проверка наличия названия созданного канала в таблице каналов
    forms_settings.channel_form_fill(
        driver,
        name_channel="Мой город",
        sub_tab_name="Каналы",
        option_name="Telegram",
        address="https://t.me/afisha_voronezh/797",
        save=True
    )

    # Открытие формы канала "Мой город", редактирование указанных полей и проверка изменений в таблице каналов
    forms_settings.change_form(
        driver,
        name_channel="Мой город",
        form_name="Изменить канал",
        new_name=None,
        option_name=None,
        address="Какая-то ссылка",
        save=False,
        sub_tab_name="Каналы"
    )

    # Проверка соответствия ссылки, изменение которой было отменено в форме, ссылке в таблице каналов
    link_address = driver.find_element("xpath", "//span[text()='Мой город']/following::a/span").text
    assert link_address == "https://t.me/afisha_voronezh/797", \
        "Ссылка канала 'Мой город' не соответствует измененному идентификатору в форме."
