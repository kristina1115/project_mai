import pytest
import logging
from selenium import webdriver
from config import url

# Настройка логирования
logging.basicConfig(level=logging.INFO)


@pytest.fixture()
def driver(request):
    # logging.info("Создаём новый драйвер...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    def fin():
        # logging.info("Закрываем драйвер...")
        driver.quit()

    request.addfinalizer(fin)
    return driver


"""
Еще 2 способа создания фикстуры для открытия и закрытия браузера:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService # Service - класс, который появился в selenium4, 
from webdriver_manager.chrome import ChromeDriverManager               # он котролирует установку, открытие и закрытие 
                                                                       # драйвера

@pytest.fixture()
def driver_start_finish():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # создаем объект service с классом 
    yield driver                                                                      # Service, куда отправляем 
    driver.quit()                                                                     # реализацию установки драйвера 
                                                                                      # через ChromeDriverManager

@pytest.fixture()
def driver_start_finish():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
"""
