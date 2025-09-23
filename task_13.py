import time
from collections import OrderedDict
from filecmp import clear_cache
from functools import wraps

def cached(max_size=None, seconds=None):
    if not isinstance(max_size, (int, type(None))):
        max_size = None
    if not isinstance(seconds, (int, float, type(None))):
        seconds = None

    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            current_time = time.time()

            if key in cache:
                result, timestamp = cache[key]

                if seconds is not None and current_time - timestamp > seconds:
                    del cache[key]
                else:
                    cache.move_to_end(key)
                    return result

            result = func(*args, **kwargs)
            cache[key] = (result, current_time)

            if max_size is not None and len(cache) > max_size:
                cache.popitem(last=False)
            return result

        def clear_cache():
            cache.clear()

        def cache_info():
            return {
                "size": len(cache),
                "max_size": max_size,
                "seconds": seconds,
                "key": list(cache.keys())
            }

        wrapper.clear_cache = clear_cache
        wrapper.cache_info = cache_info
        return wrapper
    return decorator

#Тестирование
if __name__ == "__main__":
    @cached(max_size=3, seconds=10)
    def slow_function(x):
        print(f"Вычисляю для {x}...")
        return x ** 2


    # Первый вызов — вычисляется
    print(slow_function(2))  # Вывод: "Вычисляю для 2..." → 4

    # Повторный вызов с теми же аргументами — берётся из кэша
    print(slow_function(2))  # Вывод: 4 (без вычисления)

    # Вызов с другими аргументами
    print(slow_function(3))  # Вывод: "Вычисляю для 3..." → 9
    print(slow_function(4))  # Вывод: "Вычисляю для 4..." → 16

    # Проверка ограничения размера кэша (max_size=3)
    print(slow_function(5))  # Вывод: "Вычисляю для 5..." → 25
    # Самый старый результат (для 2) должен быть удален из кэша

    # Проверка времени жизни
    time.sleep(15)
    print(slow_function(3))  # Вывод: "Вычисляю для 3..." → 9 (кэш устарел)


    # Тест с именованными аргументами
    @cached(max_size=2, seconds=5)
    def named_args_func(a, b=1):
        print(f"Вычисляю для a={a}, b={b}...")
        return a + b


    print(named_args_func(1, b=2))  # Вывод: "Вычисляю для a=1, b=2..." → 3
    print(named_args_func(1, b=2))  # Вывод: 3 (из кэша)
    print(named_args_func(1))  # Вывод: "Вычисляю для a=1, b=1..." → 2

    # Методы управления кэшем
    print(slow_function.cache_info())
    slow_function.clear_cache()