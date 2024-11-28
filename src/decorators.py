from functools import wraps
from time import time

def log(filename=None):
    def decorator_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time()
            try:
                result = func(*args, **kwargs)
                end_time = time()
                execution_time = end_time - start_time
                message = f"{func.__name__} OK, Execution time: {execution_time:.4f} seconds\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message)
                else:
                    print(message)
            except Exception as e:
                error_message = f"Ошибка функции {func.__name__}: {e}. Input: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_message)
                else:
                    print(error_message)
                return None
            return result
        return wrapper
    return decorator_func

