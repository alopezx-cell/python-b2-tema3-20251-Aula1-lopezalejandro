"""
Enunciado:
Desarrolla un sistema orientado a objetos en Python que permita gestionar productos de diferentes categorías (Libros,
Electrónicos y Ropa) en un pedido. Cada tipo de producto deberá incluir métodos específicos para describir sus
atributos únicos, así como un mecanismo para ajustar y obtener el precio, asegurando que este no sea negativo. El
diagrama UML de las clases a implementar se encuentra en 'images/UML_ej3a1.png'

Las clases y métodos a implementar son los siguientes:

- Una clase abstracta Product que define la estructura básica de un producto, incluyendo su nombre, precio, y un método
abstracto describe_product() para obtener una descripción del producto.
- Clases concretas Book, Electronic, y Clothing que heredan de Product y sobrescriben el método describe_product() para
incluir detalles específicos de cada tipo de producto, como autor y ISBN para libros, marca y modelo para electrónicos,
y talla y color para ropa.
- Un atributo price con su respectivo getter y setter en la clase Product para obtener y establecer el precio del producto,
con una validación que impide precios negativos.
- Una clase Order que permite agregar productos de cualquier tipo a un pedido y calcular el precio total del pedido.

Ejemplo:
    order = Order()
    order.add_product(Book("The Little Prince", 20, "Antoine de Saint-Exupéry", "978-3-16-148410-0"))

Salida esperada:
- El precio total del pedido.
- Una descripción detallada de cada producto en el pedido, incluyendo su categoría, nombre, detalles específicos (como
autor, marca, talla, etc.), y precio.
"""


from abc import ABC, abstractmethod
from typing import List


class Product(ABC):
    def __init__(self, name: str, price: float) -> None:
        self._name = name
        self._price = price

    @abstractmethod
    def describe_product(self) -> str:
        pass

    @property
    def price(self) -> float:
        """Getter for price."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Setter for price, ensures the price is not negative."""
        if value < 0:
            raise ValueError("El precio no puede ser negativo")
        self._price = value


class Book(Product):
    def __init__(self, name: str, price: float, author: str, isbn: str) -> None:
        super().__init__(name, price)
        self.author = author
        self.isbn = isbn

    def describe_product(self) -> str:
        return f"Book: {self._name}, Author: {self.author}, ISBN: {self.isbn}, Price: ${self.price}"


class Electronic(Product):
    def __init__(self, name: str, price: float, brand: str, model: str) -> None:
        super().__init__(name, price)
        self.brand = brand
        self.model = model

    def describe_product(self) -> str:
        return f"Electronic: {self._name}, Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"

class Clothing(Product):
    def __init__(self, name: str, price: float, size: str, color: str) -> None:
        super().__init__(name, price)
        self.size = size
        self.color = color

    def describe_product(self) -> str:
        return f"Clothing: {self._name}, Size: {self.size}, Color: {self.color}, Price: ${self.price}"


class Order:
    def __init__(self) -> None:
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Adds a product to the order."""
        self.products.append(product)

    def calculate_total(self) -> float:
        """Calculates the total price of all products in the order."""
        total = 0.0
        for p in self.products:
            total += p.price
        return total

# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     order = Order()
#     order.add_product(Book("The Little Prince", 20, "Antoine de Saint-Exupéry", "978-3-16-148410-0"))
#     order.add_product(Electronic("Smartphone", 799.99, "Apple", "X1000"))
#     order.add_product(Clothing("T-shirt", 18.99, "M", "Black"))

#     for product in order.products:
#         print(product.describe_product())
#     print(f"{f'Total order price: ${order.calculate_total()}':*^50}")
