'''
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.

input number 1
input number 2
choice for operation
-> possible errors
-> divide by zero!
'''

print("Calculadora: necesito dos números y el tipo de operación de quieres.")
n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
c = input("¿Que operación quieres? s -> suma, r -> resta, m -> multiplicacion, d -> división. ")
choices = "srmd"
c = c.lower()
if c not in choices:
  print("Por favor, elige s, r, m, o d.")
if n2 == 0 and c == 'd':
  print("No podemos dividir por 0.")
  
if c == "s":
  calc = n1 + n2
if c == "r":
  calc = n1 - n2
if c == "m":
  calc = n1 * n2
if c == "d":
  calc = n1 / n2
  
print(f"La operación {c} de {n1} y {n2} nos da: {calc}.")


