'''
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.

if no odd number function, divide by 2 and take int into SUM 
'''
i = 1
j = 100
sum = 0
while i <= j:
  div = i/2 
  if div.is_integer() == True:
    sum += div
    # print(f"--> {sum}")
  i+=1

print(f"The total is: {sum}")
