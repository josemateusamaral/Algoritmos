nota = input('Digite o nome de uma nota musical para saber a sua frequencia em hertz: ')
n = nota[0]
o = int(nota[1])
f = None

if n == 'C': f = 261.63 / ( 2 ** (4 - o) )
elif n == 'D': f = 293.66 / ( 2 ** (4 - o) )
elif n == 'E': f = 329.63 / ( 2 ** (4 - o) )
elif n == 'F': f = 349.23 / ( 2 ** (4 - o) )
elif n == 'G': f = 392.00 / ( 2 ** (4 - o) )
elif n == 'A': f = 440.00 / ( 2 ** (4 - o) )
elif n == 'B': f = 493.88 / ( 2 ** (4 - o) )
	
print(f'A frequência da nota {nota} é {f} hertz')