'''
Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.
F = (C * 1.8) + 32
celsius is the variable to adjust to test the code
'''

def convert_to_f(c):
    f = (c * 1.8) + 32
    return f


celsius = 20
c2f = convert_to_f(celsius)
print(f"{celsius} grado(s) Celsius corresponden a {c2f} Farenheit.")