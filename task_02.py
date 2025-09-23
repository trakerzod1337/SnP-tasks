def coincidence(lst=None, rng=None):
    if lst is None or rng is None:
        return []

    if not isinstance(rng, range):
        return []

    result = []
    start = rng.start
    stop = rng.stop
    step = rng.step if range.step is not None else 1

    for item in lst:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            if start <= item < stop:
                if step == 1:
                    result.append(item)
                else:
                    if (item - start) % step == 0 or isinstance(item, float):
                        result.append(item)

    return sorted(result)

#Тестирование
print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([-1, 2, 5, 124, 124124], range(-50, 500, 2)))
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))

print(coincidence([], range(1, 10)))  # []
print(coincidence([-5, -3, 0, 2, 4], range(-4, 3)))  # [-3, 0, 2]
print(coincidence([1, 2, 3, 4, 5, 6], range(2, 7, 2)))  # [2, 4, 6]
print(coincidence([1, 2, 3, 4, 5, 6, 7, 8, 9], range(3, 10, 3)))  # [3, 6, 9]
