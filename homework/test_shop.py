"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity - 1)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(product.quantity)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_cart_product(self, product, cart):
        #Проверка на добавление товара в корзину, а также на количество добавленного товара в корзине
        cart.add_product(product)
        assert product in cart.products
        assert cart.products.get(product) == 1

    def test_remove_full_cart_product(self, product, cart):
        #проверка на очистку корзины при remove_count = None
        cart.add_product(product)
        assert product in cart.products
        cart.remove_product(product)
        assert product not in cart.products

    def test_remove_some_cart_product(self, product, cart):
        # проверка на удаление из корзины remove_count продукта
        cart.add_product(product, buy_count=4)
        assert product in cart.products
        cart.remove_product(product, 3)
        assert cart.products.get(product) == 1

    def test_remove_count_cart_product(self, product, cart):
        # проверка на удаление продукта из корзины, если remove_count больше количества товара
        cart.add_product(product, buy_count=4)
        assert product in cart.products
        cart.remove_product(product, 5)
        assert product not in cart.products
        #assert cart.products.get(product) == None

    def test_clear_cart(self, product, cart):
        #проверка на полную очистку корзины
        cart.add_product(product, buy_count=5)
        assert cart.products.get(product) == 5
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, product, cart):
        #проверка на получение фулл стоимости корзины
        cart.add_product(product, buy_count=10)
        assert cart.products.get(product) == 10
        assert cart.get_total_price(product) == 1000

    def test_buy_product_in_cart(self, product, cart):
        #проверка на покупку quantity продуктов в корзине
        cart.add_product(product, buy_count=10)
        assert cart.products.get(product) == 10
        cart.buy(quantity=5)
        assert cart.products.get(product) == 5

    def test_buy_product_in_cart_ValueError(self, product, cart):
        #проверка на покупку большего quantity продуктов в корзине, вызывая VallueError
        cart.add_product(product, buy_count=5)
        with pytest.raises(ValueError):
            cart.buy(quantity=6)


