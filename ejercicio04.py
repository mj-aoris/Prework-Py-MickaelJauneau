'''
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario
one variable for the vocals
one variable as input
go through each letter
'''

def count_vocals(palabra):
    #len_palabra = len(palabra)
    vocals = "aeiou"
    count_v = 0
    i = 0
    while i <= len(palabra)-1:
      the_letter = palabra[i]
      if the_letter in vocals:
        count_v +=1
      i += 1
    return count_v
  
palabra = input("La palabra a evaluar: ")
vocal_counter = count_vocals(palabra)
print(f"The number of vocals contained in **{palabra}** is {vocal_counter}")  