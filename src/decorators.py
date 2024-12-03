from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор логирующий начало и конец функции, а так же ее результаты и возникшие ошибки"""

    def decorator_func(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Optional[Any]:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} OK\n"
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
                raise
            return result

        return wrapper

    return decorator_func
