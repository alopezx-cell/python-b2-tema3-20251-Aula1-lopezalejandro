"""
Enunciado:
Implementa una fabrica de decoradores DecoratorFactoryLogs con tres decoradores:
log_decorator, debug_log_decorator y save_log_decorator.
"""


import logging
from functools import wraps
from typing import Callable, Any
import os

# directorio para guardar los logs
log_directory: str = "data/output/logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logging.basicConfig(
    filename=os.path.join(log_directory, "app.log"),
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class DecoratorFactoryLogs:
    def log_decorator(self, message: str = "") -> Callable:
        """Registra inicio y fin de la funcion."""

        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                logging.info(
                    f"{message} Starting: {func.__name__} with args: {args}, kwargs: {kwargs}"
                )
                res = func(*args, **kwargs)
                logging.info(f"{message} Finishing: {func.__name__}")
                return res

            return wrapper

        return decorator

    def debug_log_decorator(self, message: str = "") -> Callable:
        """Registra info de debug con args y kwargs."""

        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                args_repr = [repr(a) for a in args]
                kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
                firma = ", ".join(args_repr + kwargs_repr)
                logging.debug(f"{message} Executing: {func.__name__}({firma})")
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def save_log_decorator(
        self,
        message: str = "",
        filepath: str = os.path.join(log_directory, "custom_log.log"),
    ) -> Callable:
        """Guarda el log en un archivo personalizado."""

        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                logger_custom = logging.getLogger(func.__name__)
                manejador = logging.FileHandler(filepath)
                fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
                manejador.setFormatter(fmt)
                logger_custom.addHandler(manejador)
                logger_custom.setLevel(logging.INFO)
                logger_custom.info(
                    f"{message} Executing: {func.__name__} with args: {args}, kwargs: {kwargs}"
                )
                res = func(*args, **kwargs)
                logger_custom.removeHandler(manejador)
                return res

            return wrapper

        return decorator


factory = DecoratorFactoryLogs()


@factory.log_decorator(message="Log Decorator:")
def add(a: int, b: int) -> int:
    return a + b


@factory.debug_log_decorator(message="Debug Decorator:")
def subtract(a: int, b: int) -> int:
    return a - b


@factory.save_log_decorator(
    message="Custom Log Decorator:",
    filepath=os.path.join(log_directory, "custom_operation.log"),
)
def multiply(a: int, b: int) -> int:
    return a * b

# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     print("Addition:", add(2, 3))
#     print("Subtraction:", subtract(10, 5))
#     print("Multiplication:", multiply(2, 4))
#     print("Logs saved in:", log_directory)
