'''
Ejercicio 18: Contador de Palabras
Ejercicios Introducción a Python: Enunciados 3
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.

Identiicación de palabras: separadas por espacios. Contar espacias (+1 for the last one)
'''
def count_words(text):
    l = len(text)-1
    count_s = 0 #count space
    i = 0
    while i <= l:
      char = text[i]
      if char == " ":
        count_s +=1
      i += 1
    return count_s  

text = str(input("El texto: "))
count_s = count_words(text)
count_w = count_s+1
print(f"El texto contiene {count_w} palabra(s).")
