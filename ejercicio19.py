'''
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.

use cal functions to get numbe of days in Feb.

'''
y = int(input("Año a verificar: "))
import calendar
feb = calendar.monthrange(y,2)
d = int(feb[1])

if d == 29:
  print(f"{y} es un año bisiestro.")
else:
  print(f"{y} no es un año bisiestro.")
