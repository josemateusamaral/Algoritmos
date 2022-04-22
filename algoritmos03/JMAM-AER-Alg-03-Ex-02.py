anos = float(input('Digite a idade do cachorro em anos humanos: '))
idade = 0

if anos < 0:
	print('Os anos humanos nao podem ser negativos')
elif anos <= 2:
	idade = anos * 10.5
else:
	idade = ((anos - 2) * 4) + 21
	
print(anos,' em anos de cachorro é ',idade)