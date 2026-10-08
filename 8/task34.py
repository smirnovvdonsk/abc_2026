# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.

from typing import List, Set, Tuple, Iterable
from task33 import Product

class Order:
    __products: Set[Product]

    def __init__(
            self,
            products: Iterable[Product] = []
            ):
        self.__products = set(products)

    def get_products(
            self,
            *,
            name_contains: str = '',
            price_from: int | float = float('-inf'),
            price_to: int | float = float('inf'),
            ) -> List[Product]:
        return [
            product
            for product in self.__products
            if (name_contains.lower() in product.name.lower()) and (price_from <= product.price <= price_to)
        ]

    @property
    def products(self) -> List[Product]:
        return self.get_products()

    def add_product(self, product: Product | Iterable[Product]):       
        products_to_add = [product] if isinstance(product, Product) else product
        for p in products_to_add:
            self.__products.add(p)

    def add_products(self, product: Product | Iterable[Product]):
        return self.add_product(product)

    def remove_product(self, product: Product | Iterable[Product]):       
        products_to_remove = [product] if isinstance(product, Product) else product
        for p in products_to_remove:
            if p in self.__products:
                self.__products.remove(p)

    def remove_products(self, product: Product | Iterable[Product]):
        return self.remove_product(product)

    @property
    def total_price(self) -> float:
        result = 0.0
        for product in self.__products:
            result += product.price
        return result

    

# Пример использования
book = Product("Book", 10)
pen = Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)
print(f"Общая стоимость: {order.total_price}")  # 12

order = Order(
    (
        Product("Computer", 1000),
        Product("Table", 100),
        Product("Book", 10),
        Product("Pen", 2)
    )
)
print(f"Общая стоимость: {order.total_price}")
too_expensive_products = order.get_products(price_from=999)
order.remove_products(too_expensive_products)
pen_products = order.get_products(name_contains='pen')
order.remove_products(pen_products)
print(f"Общая стоимость: {order.total_price}")
order.add_product(pen_products)
print(f"Общая стоимость: {order.total_price}")
