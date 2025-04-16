import pytest
from selenium.webdriver.common.by import By
from Locators import main_page, menu_report, menu_settings
from fixture.conftest import browser_setup2
from Metods import auth_methods, common, help_methods
from fixture import conftest
import time


@pytest.mark.usefixtures("browser_setup2")
def test_help_day_picture(browser_setup2):
    """Тест для раздела 'Картина дня'"""
    driver = browser_setup2
    print("\n=== Тест 'Картина дня' ===")

    # Авторизация (уже открывает "Картину дня")
    assert common.check_site(driver), "Неверный сайт"
    auth_methods.login(driver, conftest.Login, conftest.Password)

    #Проверка успешного входа
    picture_day = common.wait_element(driver, main_page.PICTURE_DAY, condition="visible")
    assert picture_day.text == "Картина дня", f"Неверный текст элемента: {picture_day.text}"

    # Проверка
    results = help_methods.check_help_flow(driver)

    # Закрытие схемы
    assert help_methods.close_help_schema(driver), "Не удалось закрыть схему"

    # Отчет
    for name, status, msg in results:
        assert status, f"{name}: {msg}"
    print("✅ Тест завершен успешно")


def test_help_report(browser_setup2):
    driver = browser_setup2
    print('\n== Тест "Отчёт" ==')

    # Авторизация
    assert common.check_site(driver), "Неверный сайт"
    auth_methods.login(driver, conftest.Login, conftest.Password)

    # 1. Основная страница "Отчёт"
    status, msg = help_methods.navigate_to_page(
        driver,
        menu_locator=main_page.MENU_REPORT,
        page_locator=menu_report.AUDITORE,
        page_name="Отчёт (основная)"
    )
    print(msg)
    assert status, msg

    # 2. Проверка схемы (автоматически закроет её)
    status, msg = help_methods.check_help_on_page(page_name="Отчёт (основная)")
    print(msg)
    assert status, msg

    # 3. Подстраницы
    subpages = [
        ("Отчёт → Подстраница 1", menu_report.BTN_SUBPAGE_1, menu_report.LOCATOR_SUBPAGE_1),
        ("Отчёт → Подстраница 2", menu_report.BTN_SUBPAGE_2, menu_report.LOCATOR_SUBPAGE_2),
        ("Отчёт → Подстраница 3", menu_report.BTN_SUBPAGE_3, menu_report.LOCATOR_SUBPAGE_3)
    ]

    for name, btn_locator, check_locator in subpages:
        # Переход
        status, msg = help_methods.navigate_to_page(
            driver,
            menu_locator=btn_locator,
            page_locator=check_locator,
            page_name=name
        )
        print(msg)
        assert status, msg

        # Проверка схемы
        status, msg = help_methods.check_help_on_page(page_name=name)
        print(msg)
        assert status, msg