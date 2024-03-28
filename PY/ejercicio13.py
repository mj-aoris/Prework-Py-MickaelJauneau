'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.

Divide by all potential numbers?

'''
def prime_num(num):
  for n in range(2,num):
    if num % n == 0:
      return False
  return True
    

num = int(input("Número a verificar: "))
prime = prime_num(num)
if prime == False:
  print(f"{num} no es un número primo.")

if prime == True:
  print(f"{num} es un número primo.")
