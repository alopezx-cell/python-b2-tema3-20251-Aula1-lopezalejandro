"""
Enunciado:
Desarrolla un decorador de función para medir el tiempo de ejecución de la función decorada
la finalidad es calcular el tiempo que toma guardar un DataFrames de Pandas en formatos: 
(JSON, CSV y Excel).
"""


import time
from typing import Tuple, Dict, Any, Callable
import pandas as pd
from pathlib import Path


def measure_time(func: Callable) -> Callable:
    """
    Decorator that measures the execution time of the decorated function and returns the execution time along with the function's original result.
    """

    def wrapper(*args, **kwargs) -> Tuple[Any, float]:
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        t = fin - inicio
        print(f"Execution time of {func.__name__}: {t} seconds.")
        return resultado, t

    return wrapper


@measure_time
def df_to_json(df: pd.DataFrame, filename: str, path_output: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    params = {"orient": "records", "lines": True}
    print(path_output / filename)
    df.to_json(path_output / filename, **params)
    loaded_df = pd.read_json(path_output / filename, lines=True, orient=params["orient"])
    return loaded_df, params


@measure_time
def df_to_csv(df: pd.DataFrame, filename: str, path_output: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    params = {"sep": ";", "header": None, "encoding": "utf-8"}
    df.to_csv(path_output / filename, **params)
    loaded_df = pd.read_csv(
        path_output / filename,
        sep=params["sep"],
        header=params["header"],
        encoding=params["encoding"],
    )
    return loaded_df, params


@measure_time
def df_to_excel(df: pd.DataFrame, filename: str, path_output: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    params = {"sheet_name": "Pandas to Excel"}
    df.to_excel(path_output / filename, sheet_name=params["sheet_name"], index=False)
    loaded_df = pd.read_excel(path_output / filename, sheet_name=params["sheet_name"])
    return loaded_df, params


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     path = Path(__file__).parent
#     test_csv_filename = path / "data/german_credit_data.csv"
#     path_output = path / "data/output"
#     path_output.mkdir(parents=True, exist_ok=True)
#     df_credit = pd.read_csv(test_csv_filename)
#     df_from_json, used_params_json = df_to_json(df_credit, "df_to_json_credit.json", path_output)
#     df_from_csv, used_params_csv = df_to_csv(df_credit, "df_to_csv_credit.csv", path_output)
#     df_from_excel, used_params_excel = df_to_excel(df_credit, "credit.xlsx", path_output)
