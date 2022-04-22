l1 = float(input('Digite o comprimento do primeiro lado do triângulo: '))
l2 = float(input('Digite o comprimento do segundo lado do triângulo: '))
l3 = float(input('Digite o comprimento do terceiro lado do triângulo: '))
print()

if l1 == l2 and l2 == l3:
	print('O triângulo é equilátero pois todos os lados tem o mesmo comprimento')
	
elif ( l1 == l2 ) or ( l1 == l3 ) or ( l2 == l3 ):
	print('O triângulo é isóceles pois apenas dois lados tem o mesmo comprimento')

elif l1 != l2 and l1 != l3 and l2 != l3:
	print('O triângulo é escaleno pois todos os lados tem comprimentos diferentes')