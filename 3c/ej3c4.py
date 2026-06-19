"""
Enunciado:
Usar functools.partial para crear versiones especializadas de apply_discount:
vip_discount (20%) y new_customer_discount (10%).
"""


from functools import partial


def apply_discount(price: float, discount: float) -> float:
    """Aplica un descuento al precio y devuelve el precio final."""
    precio_final = price - (price * discount / 100)
    return precio_final


vip_discount = partial(apply_discount, discount=20)
new_customer_discount = partial(apply_discount, discount=10)


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     original_price = 100
#     vip_price = vip_discount(original_price)
#     new_customer_price = new_customer_discount(original_price)
#     print(f"Original Price: {original_price}")
#     print(f"VIP Price: {vip_price}")
#     print(f"New Customer Price: {new_customer_price}")
