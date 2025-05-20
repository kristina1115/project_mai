import pytest

from OOP.conftest import browser
from OOP.pages.product_page import ProductPage
from OOP.pages.cart_page import CartPage


@pytest.mark.usefixtures('browser')
def test_add_product_to_cart(browser):
    # 1. Открываем страницу товара
    product_page = ProductPage(browser)
    product_page.open()

    # 2. Получаем название товара
    product_name = product_page.get_product_name()

    # 3. Добавляем товар в корзину
    product_page.add_to_cart()

    # 4. Переходим в корзину
    product_page.go_to_cart()

    # 5. Проверяем, что товар добавился
    cart_page = CartPage(browser)
    assert product_name in cart_page.get_cart_items(), "Товар не добавлен в корзину!"