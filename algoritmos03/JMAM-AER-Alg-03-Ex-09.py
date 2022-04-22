mes = input('Digite um mês entre [ janeiro - fevereiro - março - abril - maio - junho - julho - agosto - setembro - outubro - novembro - dezembro ] \nmês: ')
dia = int(input('Digite o dia do mês\ndia: '))
print()

if mes == 'janeiro' and dia == 1:
	print('Dia da Confraternização universal é em 1o. de janeiro')
	
elif mes == 'abril' and dia == 21:
	print('Dia de Tiradentes é em 21 de abril')
	
elif mes == 'maio' and dia == 1:
	print('Dia do trabalho é em  1o. de maio')
	
elif mes == 'setembro' and dia == 7:
	print('Dia da Independência do Brasil é em 7 de setembro')
	
elif mes == 'outubro' and dia == 12:
	print('Dia da Nossa Senhora Aparecida é em 12 de outubro')

elif mes == 'novembro' and dia == 2:
	print('Dia de Finados é em 2 de novembro')
	
elif mes == 'novembro' and dia == 15:
   print('Dia da Proclamação da República é em 15 de novembro')
   
elif mes == 'dezembro' and dia == 25:
   print('O Natal é em 25 de dezembro')

else:
	print('Não há feriados no dia ',dia,' de ',mes)