"""
Enunciado:
Desarrolla un decorador de clase en Python que registre en un log cada vez que una función
es llamada, mostrando el nombre y los argumentos. Se puede desactivar con print_logs=False.
"""

from pathlib import Path
import logging
from types import MethodType
from typing import Callable, Any
import pandas as pd

logging.basicConfig(level=logging.INFO)
PRINT_LOGS: bool = True


class LogMethodCalls(object):
    def __init__(self, print_logs: bool = True) -> None:
        self.print_logs = print_logs

    def __call__(self, func: Callable) -> Callable:
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            if self.print_logs:
                args_repr = [repr(a) for a in args]
                kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
                signature = ", ".join(args_repr + kwargs_repr)
                logging.info("Calling %s (%s)", func.__name__, signature)
            return func(*args, **kwargs)

        return wrapped

    def __get__(self, instance: Any, cls: Any) -> Any:
        return self if instance is None else MethodType(self, instance)


@LogMethodCalls(print_logs=PRINT_LOGS)
def load_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


@LogMethodCalls(print_logs=PRINT_LOGS)
def load_and_describe_csv(filename: str) -> pd.DataFrame:
    dataframe = pd.read_csv(filename)
    return dataframe.describe()


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     path_parent = Path(__file__).parent
#     FILENAME_PATH = path_parent / 'data/german_credit_data.csv'
#     dataframe_credit = load_csv(FILENAME_PATH)
#     print(dataframe_credit.head(1))
#     description = load_and_describe_csv(FILENAME_PATH)
#     print(description)
