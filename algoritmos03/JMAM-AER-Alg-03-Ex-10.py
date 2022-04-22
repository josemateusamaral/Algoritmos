pos = input('Digite uma posição do tabuleiro de xadrez: ')
col = pos[0]
lin = int(pos[1])
color = lin % 2

if col == 'a' or col == 'c' or col == 'e' or col == 'g':
	color = not color

if color:
	print('A cor da posição ',pos,' é branca')
else:
	print('A cor da posição ',pos,' é preta')
	