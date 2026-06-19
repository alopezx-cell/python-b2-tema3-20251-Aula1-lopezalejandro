"""
Enunciado:
Conversion de temperaturas de Celsius a Fahrenheit usando lambda, filter y map.
Se filtran las que son mayores o iguales a 60 porque son errores de medicion.
"""

temperatures_celsius = [54, 84, 38, 104, 101, 107, 55, 1, 38, 31, 109, 6, 91, 46, 16, 28, 74, 102, 20, 39]
# filtramos los valores erroneos (>=60)
filter_temperatures_celsius = list(filter(lambda x: x < 60, temperatures_celsius))
convert_to_fahrenheit = lambda celsius: (celsius * 9/5) + 32
temperatures_fahrenheit = list(map(convert_to_fahrenheit, filter_temperatures_celsius))

# Para probar el código, descomenta las siguientes líneas
# print("Temperatures in Celsius:", temperatures_celsius)
# print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
