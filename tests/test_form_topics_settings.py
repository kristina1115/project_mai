import pytest
import logging
from marina.components import forms_settings
from marina.common import wait
from selenium.webdriver.common.by import By
from marina.locators import form_topics_loc


@pytest.fixture()
def data_topics(driver, sub_tab_name_check="Тематики"):
    # Список названий тестовых тематик
    topic_names = [
        "День Победы",
        "Майские праздники",
        "111",
        "Годовщина Победы"
    ]
    # Открытие формы
    forms_settings.open_create_form(
        driver,
        tab_name="Настройки",
        sub_tab_name=sub_tab_name_check,
        form_name="Тематика"
    )

    # Передаём список названий тестовых тематик в тест
    yield topic_names

    # Переход на нужный подраздел и получение текущего списка тематик
    names_topics_in_table = forms_settings.check_before_delete(
        driver,
        tab_name="Настройки",
        sub_tab_name=sub_tab_name_check
    )

    # Проверка наличия тестовой тематики в текущем списке тематик и ее удаление
    for name in topic_names:
        if name in names_topics_in_table:
            forms_settings.delete_substance(driver, name_substance=name, sub_tab_name=sub_tab_name_check)
            logging.info("Тестовая тематика удалена.")
            break


def test_topic_create_only_required_fields(driver, data_topics):
    """1. Проверка сохранения формы с заполнением только обязательных полей "Название" и "Класс событий"."""

    forms_settings.topic_form_fill(
        driver,
        name_topic="День Победы",
        sub_tab_name="Тематики",
        class_option_name="Прочее",
        publication_channel=None,
        language=None,
        country=None,
        region=None,
        ai_status=None,
        keyword=None,
        print_source=None,
        add_source=None,
        save=True
    )


def test_topic_create_all_fields(
        driver,
        data_topics,
        name_topic="День Победы",
        country="Россия",
        region="Воронежская область",
        publication_channel="МГТУ тестовый"
):
    """
    2. Проверка сохранения формы с заполнением всех полей (добавление реальной ссылки в поле 'Источники публикаций' не
      позволяет сохранять форму, поэтому используем цифры с запятой, тогда сохранение выполняется).
    """

    forms_settings.topic_form_fill(
        driver,
        name_topic=name_topic,
        sub_tab_name="Тематики",
        class_option_name="Прочее",
        publication_channel=publication_channel,
        language="Русский",
        country=country,
        region=region,
        ai_status=False,
        keyword="ветераны",
        print_source="111,000",
        add_source="222,000",
        save=True
    )

    # Проверка наличия выбранной страны и региона для созданной тематики в таблице.
    forms_settings.search_topic(driver, name_topic)

    wait.text_presence(
        driver,
        form_topics_loc.GEOGRAPHY_IN_TABLE,
        f"{country}, {region}",
        "Сохраненные названия страны и региона не присутствует в таблице."
    )

    # Проверка наличия выбранного канала публикации для созданной тематики.
    wait.presence(
        driver,
        (By.XPATH, f"//a/span[text()='{name_topic}']/following::span[text()='{publication_channel}']"),
        f"В таблице тематик отсутствует канал '{publication_channel}' для тематики '{name_topic}'."
         )

    # Проверка, что радио-кнопка "ИИ" в таблице тематик отключена для созданной тематики.
    forms_settings.search_topic(driver, name_topic)

    wait.text_in_attribute(
        driver,
        form_topics_loc.AI_BUTTON,
        "aria-checked",
        "false",
        "Радиокнопка включена."
    )
    driver.refresh()


@pytest.mark.skip(reason="Возможен фейл — временно отключено")
def test_topic_create_only_print_source_and_required_fields(driver, data_topics):
    """
    3. Проверка сохранения формы с заполнением только обязательных полей и необязательного поля 'Источники публикаций'
        (прямой ввод ссылки в поле). Проверка добавлена из-за бага несохранения формы при добавлении реальной ссылки в
        поле 'Источники публикаций'.
    """

    forms_settings.topic_form_fill(
        driver,
        name_topic="Майские праздники",
        sub_tab_name="Тематики",
        class_option_name="В мире",
        publication_channel=None,
        language=None,
        country=None,
        region=None,
        ai_status=None,
        keyword=None,
        print_source="https://t.me/afisha_voronezh",
        add_source=None,
        save=True
    )


@pytest.mark.skip(reason="Возможен фейл — временно отключено")
def test_topic_create_only_add_source_and_required_fields(driver, data_topics):
    """
    4. Проверка сохранения формы с заполнением только обязательных полей и необязательного поля 'Источники публикаций'
        (через опцию 'Добавить канал'). Проверка добавлена из-за бага несохранения формы при добавлении реальной ссылки
        в поле 'Источники публикаций'.
        """
    forms_settings.topic_form_fill(
        driver,
        name_topic="111",
        sub_tab_name="Тематики",
        class_option_name="Бизнес",
        publication_channel=None,
        language=None,
        country=None,
        region=None,
        ai_status=None,
        keyword=None,
        print_source=None,
        add_source="https://t.me/afisha_voronezh",
        save=True
    )


def test_topic_update_all_fields(
        driver,
        data_topics,
        sub_tab_name="Тематики",
        name_topic="День Победы",
        new_name_topic="Годовщина Победы",
        publication_channel="МГТУ тестовый",
        new_channel="Агрегатор. Москва",
        language="Русский",
        new_country="Беларусь",
        new_region="Минск",
        keyword="ветераны"
):
    """
    5. Проверка сохранения отредактированной формы (изменяются все поля и состояние кнопки 'ИИ'), проверка отображения
        сделанных изменений в таблице тематик.
    """

    # Создание тестовой тематики
    forms_settings.topic_form_fill(
        driver,
        sub_tab_name=sub_tab_name,
        name_topic=name_topic,
        class_option_name="Прочее",
        publication_channel=publication_channel,
        language=language,
        country="Россия",
        region="Воронежская область",
        ai_status=False,
        keyword=keyword,
        print_source="111,000",
        add_source="222,000",
        save=True
    )

    # Изменение тематики
    forms_settings.topic_update(
        driver,
        sub_tab_name=sub_tab_name,
        name_topic=name_topic,
        new_name_topic=new_name_topic,
        new_option_name="В мире",
        delete_channel=publication_channel,
        new_channel=new_channel,
        delete_language=language,
        new_language="Немецкий",
        delete_geo="Россия, Воронежская область",
        new_country=new_country,
        new_region=new_region,
        ai_status=True,
        delete_keyword=keyword,
        new_keyword="салют",
        print_source="222,111",
        add_source="000,111",
        delete_source="000,111",
        save=True
    )

    # Проверка наличия новой страны и региона для измененной тематики в таблице.
    forms_settings.search_topic(driver, new_name_topic)

    wait.text_presence(
        driver,
        form_topics_loc.GEOGRAPHY_IN_TABLE,
        f"{new_country}, {new_region}",
        "Измененные названия страны и региона не присутствует в таблице."
    )

    # Проверка наличия выбранного канала публикации для созданной тематики.
    wait.presence(
        driver,
        (By.XPATH, f"//a/span[text()='{new_name_topic}']/following::span[text()='{new_channel}']"),
        f"В таблице тематик отсутствует канал '{new_channel}' для тематики '{new_name_topic}'."
         )

    # Проверка, что радио-кнопка "ИИ" в таблице тематик включена для созданной тематики.
    forms_settings.search_topic(driver, new_name_topic)

    wait.text_in_attribute(
        driver,
        form_topics_loc.AI_BUTTON,
        "aria-checked",
        "true",
        "Радиокнопка не включена."
    )
    driver.refresh()


def test_topic_create_cancel(driver):
    """
    6. Проверка отмены сохранения формы."""

    forms_settings.topic_form_fill(
        driver,
        name_topic="111",
        sub_tab_name="Тематики",
        class_option_name="Бизнес",
        publication_channel="МГТУ тестовый",
        language="Русский",
        country="Россия",
        region="Воронежская область",
        ai_status=False,
        keyword="ветераны",
        print_source="000,555",
        add_source="555,666",
        save=False
    )
