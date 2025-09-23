def connect_dicts(dict1, dict2):
    sum1 = 0
    for value in dict1.values():
        sum1 += value
    sum2 = 0
    for value in dict2.values():
        sum2 += value

    if sum1 > sum2:
        great_dict = dict1
        poor_dict = dict2
    else:
        great_dict = dict2
        poor_dict = dict1

    result = {}

    for key, value in poor_dict.items():
        if value >= 10:
            result[key] = value
    for key, value in great_dict.items():
        if value >= 10:
            result[key] = value

    sort_result = dict(sorted(result.items(), key=lambda item: item[1]))
    return sort_result





#Тестирование
print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))  # => {"c": 11, "b": 12}
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))  # => {d: 11, "c": 12, "a": 13}
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))  # => {"c": 11, "b": 12, "a": 15}