'''
Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.

div mod.

'''
min = int(input("Número de minutos: "))

m = min % 60
h = int(min / 60) 

print(f"{min} minuto(s) = {h} hora(s) y {m} minuto(S)")