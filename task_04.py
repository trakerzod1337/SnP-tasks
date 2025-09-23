def sort_list(list):
    if not list:
        return []

    if len(list) == 1:
        return list + [list[0]]

    min_val = min(list)
    max_val = max(list)

    result = list.copy()

    for i in range(len(result)):
        if result[i] == min_val:
            result[i] = max_val
        elif result[i] == max_val:
            result[i] = min_val

    result.append(min_val)

    return result

#Тестирование
print(sort_list([])) # => []
print(sort_list([2, 4, 6, 8])) # => [8, 4, 6, 2, 2]
print(sort_list([1])) # => [1, 1]
print(sort_list([1, 2, 1, 3])) # => [3, 2, 3, 1, 1]