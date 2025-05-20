from OOP.pages import base_page
from selenium.webdriver.common.by import By


class ProductPage(base_page.BasePage):
    # Локаторы элементов страницы продукта
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "input[value='Add to cart']")
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-name']/h1")
    CART_LINK = (By.XPATH, "//span[@class='cart-label' and text()='Shopping cart']")

    def __init__(self, driver):
        super().__init__(driver, "https://demowebshop.tricentis.com/health")  # Пример URL товара

    def add_to_cart(self):
        """Добавить товар в корзину"""
        self.click_element(self.ADD_TO_CART_BTN)

    def get_product_name(self):
        """Получить название товара"""
        return self.get_text(self.PRODUCT_NAME)

    def go_to_cart(self):
        """Перейти в корзину"""
        self.click_element(self.CART_LINK)