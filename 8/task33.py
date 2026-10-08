# Инкапсуляция и property
# todo: Класс "Товар" (Защита от отрицательной цены)
# Создайте класс Product. У него есть свойства name (простая строка) и price.
# При установке цены проверяйте, что она не отрицательная.
# Если пытаются установить отрицательную цену, устанавливайте 0.


class Product():
    name: str
    __price: float

    def __init__(self, name: str, price: int | float = 0):
        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        return self.__price
    @price.setter
    def price(self, price: int | float):
        self.__price = float(price) if price >= 0 else 0


# Пример использования
if __name__ == '__main__':
    product = Product("Book", 10)
    print(product.price)  # 10
    product.price = -5
    print(product.price)  # 0