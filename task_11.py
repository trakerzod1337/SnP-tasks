class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self._calories = value

    def is_healthy(self):
        if self._calories is None or not isinstance(self._calories, (int, float)):
            return False
        return self._calories < 200
    def is_delicious(self):
        return True

#Тестирование
if __name__ == '__main__':
    cake = Dessert("Торт", 300)
    print(f"Название: {cake.name}")  # Торт
    print(f"Калории: {cake.calories}")  # 300
    print(f"Здоровый: {cake.is_healthy()}")  # False
    print(f"Вкусный: {cake.is_delicious()}")  # True
    print()

# Тест: Здоровый десерт
    apple = Dessert("Яблоко", 50)
    print(f"Яблоко здоровое: {apple.is_healthy()}")  # True
    print()

# Тест: Без параметров
    unknown = Dessert()
    print(f"Неизвестный десерт: {unknown.name}")  # None
    print(f"Калории: {unknown.calories}")  # None
    print(f"Вкусный: {unknown.is_delicious()}")  # True
    print(f"Здоровый: {unknown.is_healthy()}")  # False
    print()

# Тест: Изменение свойств
    dessert = Dessert()
    dessert.name = "Пирог"
    dessert.calories = 150
    print(f"После изменения: {dessert.name}, {dessert.calories}")
    print(f"Здоровый: {dessert.is_healthy()}")  # True