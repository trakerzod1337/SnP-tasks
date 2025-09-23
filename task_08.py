import math

from unicodedata import digit


def multiply_numbers(inputs = None):
    if inputs is None:
        return None
    input_str = str(inputs)

    digits = [int(char) for char in input_str if char.isdigit()]

    if not digits:
        return None

    return math.prod(digits)

#Тестирование
print(multiply_numbers())  # => None
print(multiply_numbers('ss'))  # => None
print(multiply_numbers('1234'))  # => 24
print(multiply_numbers('sssdd34'))  # => 12
print(multiply_numbers(2.3))  # => 6
print(multiply_numbers([5, 6, 4]))  # => 120
print(multiply_numbers('a1b2c3'))   # 6
print(multiply_numbers(123.45))     # 120
print(multiply_numbers(''))         # None