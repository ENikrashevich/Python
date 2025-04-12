import time
from functools import wraps


# написать декоратор, который сохраняет результат работы функции
# при заданных параметрах на 2 секунды
# проверить sleep-ами


def cached_with_time(expire_time: int):
    def decorator(func):
        cache = {}


        @wraps(func)
        def wrapper(*args, ** kwargs):
            key = (args, frozenset(kwargs.items()))
            current_time = time.time()
            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp < expire_time:
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            return result
        return wrapper
    return decorator


@cached_with_time(expire_time=2)
def func(x):
    time.sleep(0.1)
    return x*2


func(1)
