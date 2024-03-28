'''
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.
'''
def add_val(numbers):
  numbers = numbers.split()
  print(f"the list is: {numbers}")
  counter = 0
  total = 0
  for number in numbers:
    number = int(number)
    counter += 1
    total += number
  return total

#numbers =  (7,61,161,3,5,6)
numbers = input("Su lista de números, separados por espacios: ")
total = add_val(numbers)
print(f"el total de los nuúmeros es {total}.")