'''
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.

two inputs
calculations
rounding?

'''
weight = float(input("Tu peso en kilogramos: "))
height = float(input("Tu altura en centimetros: "))
height = height / 100
imc = weight / (height ** 2)
imc = round(imc,2)

print(f"Tu IMC: {imc} (peso: {weight}kg and altura: {height}m)")