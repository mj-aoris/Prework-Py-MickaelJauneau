'''
Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.

Get current date
Get birth date in 4 digits
Validate
Get difference, adjust, print

'''
def validate_year(c_year, b_year):
  if len(str(b_year)) != 4:
    print("Lo siento: necesito el año en el formato correcto.")
    exit()
  elif b_year > c_year:
    print("El año de nacimiento no puede estar en el futuro")
    exit()
  else:
    diff = c_year - b_year
    # print("Diff: ", diff)
  return diff

# Import date class from datetime module
from datetime import date 
# Returns the current local date
today = date.today()
c_year = today.strftime("%Y")
c_year = int(c_year)
b_year = int(input("Tu fecha de nacimiento en 4 digitos: "))
diff = validate_year(c_year, b_year)
diff2 = diff -1
print(f"Tienes {diff2} o {diff} años.")