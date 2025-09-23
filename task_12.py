from task_11 import Dessert

class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self.flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        if self._flavor == "black licorice":
            return False
        return True


#Тестирование
print("=== Тест 1: Обычная желейка ===")
jb1 = JellyBean("Клубничная", 50, "strawberry")
print(f"Название: {jb1.name}")           # Унаследовано от Dessert
print(f"Калории: {jb1.calories}")        # Унаследовано от Dessert
print(f"Вкус: {jb1.flavor}")             # Собственное свойство
print(f"Вкусная: {jb1.is_delicious()}")  # Переопределенный метод
print(f"Здоровая: {jb1.is_healthy()}")   # Унаследованный метод
print()

print("=== Тест 2: Черная лакрица (не вкусная) ===")
jb2 = JellyBean("Лакричная", 60, "black licorice")
print(f"Вкус: {jb2.flavor}")
print(f"Вкусная: {jb2.is_delicious()}")  # False!
print()

print("=== Тест 3: Без указания вкуса ===")
jb3 = JellyBean("Простая", 40)
print(f"Вкус: {jb3.flavor}")             # None
print(f"Вкусная: {jb3.is_delicious()}")  # True (None ≠ "black licorice")
print()

print("=== Тест 4: Изменение свойств ===")
jb4 = JellyBean("Яблочная", 55, "apple")
print(f"Изначальный вкус: {jb4.flavor}")
jb4.flavor = "black licorice"  # Меняем вкус
print(f"Новый вкус: {jb4.flavor}")
print(f"Теперь вкусная: {jb4.is_delicious()}")  # False!