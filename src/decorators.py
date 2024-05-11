import functools
from typing import Any, Callable, Optional, Tuple


def log(filename: Optional[str] = None) -> Callable[[Callable], Callable]:
    """Декоратор для логгирования действий функции"""

    def decorator(func: Callable) -> Callable:
        """Обертка декоратора для функции"""

        @functools.wraps(func)
        def wrapper(*args: Tuple[Any], **kwargs: Any) -> Any:
            """Внутренняя обертка для функции, выполняющая логирование"""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(error_message)
                    raise e
                else:
                    print(error_message)
                    return
            if filename:
                with open(filename, "a") as file:
                    file.write(log_message)
            else:
                print(log_message)
            return result

        return wrapper

    return decorator
