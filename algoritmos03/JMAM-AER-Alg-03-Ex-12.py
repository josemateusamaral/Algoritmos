ano = int(input('Digite um ano para saber se ele é um ano bissexto: '))

if ano % 400 == 0: bissexto = True
elif ano % 100 == 0: bissexto = False
elif ano % 4 == 0: bissexto = True
else: bissexto = False
	
if bissexto: print(ano,' é um ano bissexto')
else: print(ano,' não é um ano bissexto')