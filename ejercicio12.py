'''
Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.
2 inputs. float. 
validation: > 0 
no unit. 
'''
l_1 = float(input("Primer lado: "))
l_2 = float(input("Segundo lado: "))
if l_1 <= 0 or l_2 <=0:
  print("Las dimensiones tienen que ser > a cero.")
  exit()

a = l_1 * l_2
print("El área del rectángulo es: ",a)