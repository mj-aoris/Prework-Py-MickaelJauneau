'''
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.

input, extract, div module, qualify/counter
podemos configura un contador (y restar)... pero vamos con 2 contadors
'''

def val_num(numbers):
  print(f"the list is: {numbers}")
  counter = 0
  c_odd = 0
  c_even = 0
  for number in numbers:
    number = int(number)
    counter += 1
    d = number % 2
    if d != 0:
        c_odd += 1
    elif d == 0:
      c_even += 1
  return (counter,c_even,c_odd)

#numbers =  (7,61,161,3,5,6)
numbers = input("Su lista de números, separados por espacios: ")
numbers = numbers.split()
validation = val_num(numbers)
print(f"De los {validation[0]} nuúmeros, hay {validation[1]} par(es) y {validation[2]} impar(es).")