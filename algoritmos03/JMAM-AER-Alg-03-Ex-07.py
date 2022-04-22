barulho = int(input('Digite um nivel de barulho entre 40 e 130 decibéis: '))

if barulho < 40 or barulho > 130:
	print(barulho,' decibéis não esta entre a faixa permitida de 40 a 130 decibéis')
	
elif barulho == 40:
	print(barulho,' decibéis equivale ao barulho de uma sala silênciosa')

elif barulho > 40 and barulho < 70:
	print(barulho,' decibéis esta entre o barulho de uma sala silênciosa e o barulho de um despertador')

elif barulho == 70:
	print(barulho,' decibéis equivale ao barulho de um despertador')
	
elif barulho > 70 and barulho < 106:
	print(barulho,' decibéis esta entre o barulho de um despertador e o barulho de um cortador de grama')
	
elif barulho == 106:
	print(barulho,' decibéis equivale ao barulho de um cortador de grama')
	
elif barulho > 106 and barulho < 130:
	print(barulho,' decibéis esta entre o barulho de um cortador de grama e o barulho de uma britadeira')
	
elif barulho == 130:
	print(barulho,' decibéis equivale ao barulho de uma britadeira')