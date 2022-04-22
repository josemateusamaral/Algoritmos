a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
delta = ( b ** 2 ) - ( 4 * a * c )

if delta < 0:
	print('A equação não possui raizes reais')
	
elif delta == 0:
	raiz = ( b * -1 ) / ( 2 * a )
	print('A equação possui uma raiz real igual a ',raiz)
	
elif delta > 0:
	raiz1 = ( ( b * -1 ) + delta ) / ( 2 * a )
	raiz2 = ( ( b * -1 ) - delta ) / ( 2 * a )
	print(f'A equação possui duas raizes reais\nx1 = {raiz1}\nx2 = {raiz2}')