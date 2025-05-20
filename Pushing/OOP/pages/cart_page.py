from OOP.pages import base_page
from selenium.webdriver.common.by import By


class CartPage(base_page.BasePage):
    CART_ITEMS = (By.XPATH, "//td[@class='product']")  # Локатор товаров в корзине

    def __init__(self, driver):
        super().__init__(driver, "https://demowebshop.tricentis.com/cart")

    def get_cart_items(self):
        """Получить список товаров в корзине"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        return [item.text for item in items]