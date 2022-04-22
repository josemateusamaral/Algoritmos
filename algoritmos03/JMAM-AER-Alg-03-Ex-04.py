quantidadeLados = int(input('Digite a quantidade de lados do polígono para saber o tipo do polígono: '))
if quantidadeLados < 3 or quantidadeLados > 10:
	print('A quantidade de lados deve ser um número entre 3 e 10')
elif quantidadeLados == 3:
	print('Seu polígono é um triângulo')	
elif quantidadeLados == 4:
	print('Seu polígono é um quadrângulo')
elif quantidadeLados == 5:
	print('Seu polígono é um pentágono')
elif quantidadeLados == 6:
	print('Seu polígono é um hexágono')
elif quantidadeLados == 7:
	print('Seu polígono é um heptágono')
elif quantidadeLados == 8:
	print('Seu polígono é um octágono')
elif quantidadeLados == 9:
	print('Seu polígono é um eneágono')
elif quantidadeLados == 10:
	print('Seu polígono é um decágono')