'''
Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.

input float
apply 20%
'''

price = float(input("Precio del articulo: "))
discounted = price * 0.8
print(f"El precio con 20% de descuento es: {discounted}")