'''
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.

Star with age
Pass through function for evalution
Print output.
'''

def check_age(age):
  if age > 17:
      conclusion = "La persona es mayor de edad."
  else:
    conclusion = "La persona es menor de edad"
  return conclusion

age = input("Edad: ")
age = int(age)
conclusion = check_age(age)
print(conclusion)

