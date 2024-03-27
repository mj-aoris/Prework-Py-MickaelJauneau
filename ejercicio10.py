'''
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).

Create a list
Check position (-1!)
Error if > 7 
Error if < 1
INT on input
'''

def find_day(d):
  d = d-1
  days = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]
  day = days[d]
  return day

d = int(input("Día que quieres encontrar: "))
if d > 7:
  print("Solo valores de 1 a 7.")
  exit()
if d < 1:
  print("Solo valores de 1 a 7.")
  exit()

day = find_day(d)
print(f"{d} corresponde a: {day}")