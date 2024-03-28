'''
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.

input -> quantity of usd
calculation
return

'''
def cambio(dolares):
  euros = dolares * 0.85
  return euros

dolares = int(input("Dolares: "))
euros = cambio(dolares)

print(f"{dolares} dolares son {euros} euros")

