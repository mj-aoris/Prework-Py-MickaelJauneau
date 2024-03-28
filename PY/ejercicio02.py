'''
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta

Start with check & tip variables
Calculate full check

'''
def check_with_tip(check,tip):
    to_pay = check + (check * tip / 100)
    return to_pay
  
check = 100
tip = 15

full_check = check_with_tip(check,tip)
print(full_check)
