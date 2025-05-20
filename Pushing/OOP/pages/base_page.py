from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver  # экземпляр веб-драйвера (Chrome, Firefox и т. д.)
        self.url = url        # URL страницы

    def open(self):
        """Открыть страницу в браузере"""
        self.driver.get(self.url)

    def find_element(self, locator, timeout=10):
        """Найти элемент с ожиданием"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден"
        )

    def click_element(self, locator):
        """Кликнуть по элементу"""
        self.find_element(locator).click()

    def get_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text