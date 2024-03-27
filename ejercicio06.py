'''
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

Input -> length -> grab letters one by one. Compare.
'''

def reversing(palabra):
  i = len(palabra)-1
  reversed = ""
  while i >= 0:
    letter = palabra[i]
    reversed += letter
    i -=1
  return reversed
    
palabra = input("La palabra a evaluar: ")
reversed = reversing(palabra)
if palabra == reversed:
  print(f"La palabra {palabra} es un palíndromo :-)")
else: 
  print(f"La palabra {palabra} no es un palíndromo :-| ")