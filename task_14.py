class EvenNumbers:
    def __init__(self, n):
        self.n = n if isinstance(n, int) and n >= 0 else 0
        self.current = 0
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        self.count += 1
        return value

#Тестирование
evens = EvenNumbers(5)
result = []
for num in evens:
    result.append(str(num))
print(', '.join(result))
# Должно вывести 0, 2, 4, 6, 8