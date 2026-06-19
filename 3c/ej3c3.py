"""
Enunciado:
Generar todas las combinaciones posibles de contraseñas usando itertools.product.
Caracteres: 'AZ' (mayus), 'xy' (minus), '09' (digitos), '@#' (simbolos).
"""

import itertools
from typing import List


def generate_passwords(password_length: int) -> List[str]:
    # grupos de 2 caracteres cada uno
    mayusculas = "AZ"
    minusculas = "xy"
    numeros = "09"
    simbolos = "@#"
    chars = mayusculas + minusculas + numeros + simbolos
    combinaciones = itertools.product(chars, repeat=password_length)
    lista_pwds = ["".join(combo) for combo in combinaciones]
    return lista_pwds


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     PASSWORD_LENGHT = 4
#     password_list = generate_passwords(PASSWORD_LENGHT)
#     print(f"Number of passwords generated: {len(password_list)}")
#     print("First 10 passwords generated:", password_list[:10])
