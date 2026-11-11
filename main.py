#cuenta a pagar al mes
ingreso = 500
iess =9.45
conver= iess/100
print(f'Tu ingreso mensual:{ingreso}')
porcent = ingreso*conver
print(f'Aporte al iess: {porcent:.2f}')
ingreso -= porcent
print(f'Tu total cubriendo lo del iess: {ingreso:.2f}')
print('-----------------------------------------------------------------------------')
aport_home = 100
internet=18.98
netflix=12.00
gasolina=20.00
print(f'Tu aporte en casa: {aport_home} \n Pago de internet: {internet} \n Pago de netflix: {netflix} \n Pago de gasolina: {gasolina}')
gastos = aport_home + internet + netflix + gasolina
ingreso-=gastos
print(f'Tu total de gastos es: {gastos}')
print('----------------------------------------------------------------------------------------------------------------')
print(f'Tu total es: {ingreso:.2f}')



