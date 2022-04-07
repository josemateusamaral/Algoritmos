data = int(input('Digite um número de mátricula no formato AASDDD: '))
digito1 = int(data % 10)
digito2 = int((data % 100) - digito1) // 10
digito3 = int((data % 1000) - digito2) // 100
digito4 = int((data % 10000) - digito3) // 1000
digito5 = int((data % 100000) - digito4) // 10000
digito6 = int((data % 1000000) - digito5) // 100000
print(f'O ano da matricula foi: {digito6}{digito5}\nO semestre da mátricula foi: {digito4}')