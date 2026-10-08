# Инкапсуляция и property
# todo: Класс "Температура"
# Создайте класс Temperature, который хранит температуру в градусах Цельсия.
# Добавьте свойство для получения и установки температуры в Фаренгейтах и Кельвинах.
# Внутренне температура должна храниться только в Цельсиях.

# celsius (get, set) - работа с Цельсиями.
# fahrenheit (get, set) - при установке конвертирует значение в Цельсии.
# kelvin (get, set) - при установке конвертирует значение в Цельсии.



class Temperature:
    __celsius: float

    def __init__(self, celsius: int | float = 20):
        self.celsius = celsius

    @property
    def ABSOLUTE_ZERO_CELSIUS(self) -> float:
        return -273.15

    @property
    def celsius(self) -> float:
        return self.__celsius
    @celsius.setter
    def celsius(self, celsius: int | float):
        self.__celsius = float(celsius)

    @property
    def kelvin(self) -> float:
        return self.celsius - self.ABSOLUTE_ZERO_CELSIUS
    @kelvin.setter
    def kelvin(self, kelvin: int | float):
        self.celsius = float(kelvin) + self.ABSOLUTE_ZERO_CELSIUS

    @property
    def fahrenheit(self) -> float:
        return (9.0 / 5.0) * self.celsius + 32.0
    @fahrenheit.setter
    def fahrenheit(self, fahrenheit: int | float):
        self.celsius = (5.0 / 9.0) * (float(fahrenheit) - 32.0)
    

# Пример использования
t = Temperature(25)
print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
t.fahrenheit = 32
print(f"После установки 32F: {t.celsius}C")