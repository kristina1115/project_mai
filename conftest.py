import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv


load_dotenv()
url = os.getenv("url")
login = os.getenv("login")
password = os.getenv("password")


@pytest.fixture()
def driver(request):
    driver = webdriver.Chrome()
    driver.get(url)

    def fin():
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
