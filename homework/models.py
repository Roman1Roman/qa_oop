
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity=quantity):
            self.quantity -= quantity
            return True
        else:
            raise ValueError

    def __hash__(self):
        return hash(self.name + self.description)

    def __eq__(self, other):
        if isinstance(other, Product):
            return(self.name + self.description) == (other.name + other.description)
        return False


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1) -> dict:
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if remove_count == None:
            del self.products[product]
        elif self.products[product] <= remove_count:
            del self.products[product]
        else:
            self.products[product] -= remove_count



    def clear(self):
        self.products = {}

    def get_total_price(self, product: Product) -> float:
        return sum([quantity * product.price for product, quantity in self.products.items()])

    def buy(self, quantity):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for item in self.products:
            if item.check_quantity(quantity):
                self.products[item] -= quantity
                if self.products[item] < 0:
                    raise ValueError
            else:
                raise ValueError

