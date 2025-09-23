def max_odd(array):
    max_value = None

    for item in array:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            if isinstance(item, float) and item.is_integer():
                num = int(item)
            else:
                num = item

            if num % 2 != 0:
                if max_value is None or num > max_value:
                    max_value = num

    return max_value

#Тестирование
print(max_odd([1, 2, 3, 4, 4]))  # => 3
print(max_odd([21.0, 2, 3, 4, 4]))  # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))  # => 3
print(max_odd(['ololo', 'fufufu']))  # => None
print(max_odd([2, 2, 4]))  # => None