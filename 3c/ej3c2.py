"""
Enunciado:
Añadir campo reading_time a cada libro cargado del JSON usando lambda y map.
Formula: round(paginas * 250 / 200)
"""

from pathlib import Path
import json
import os
from typing import Dict, List

path = Path(__file__).parent

with open(path / "data/books_data.json", "r") as file:
    books: List[Dict] = json.load(file)["books"]

# lambda que calcula tiempo de lectura estimado
calculate_reading_time: callable = lambda book: round((book["pages"] * 250) / 200)
books_with_reading_time: List[Dict] = list(
    map(lambda book: {**book, "reading_time": calculate_reading_time(book)}, books)
)


# Para probar el código, descomenta las siguientes líneas
# save_directory: str = path / "data/output"
# if not os.path.exists(save_directory):
#     os.makedirs(save_directory)

# with open(f"{save_directory}/books_with_reading_time.json", "w") as file:
#     json.dump({"books": books_with_reading_time}, file)

# for book in books_with_reading_time[:3]:
#     print(book)
