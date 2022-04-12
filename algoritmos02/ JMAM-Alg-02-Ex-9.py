data = int(input('Digite uma data no formato DDMMAA usando um número inteiro de 5 dígitos: '))
digito1 = int(data % 10)
digito2 = int((data % 100) - digito1) // 10
digito3 = int((data % 1000) - digito2) // 100
digito4 = int((data % 10000) - digito3) // 1000
digito5 = int((data % 100000) - digito4) // 10000
digito6 = int((data % 1000000) - digito5) // 100000
print(f'\n\nA data no formato DDMMAA foi: {data}\nNo formato AAMMDD fica: {digito2}{digito1}{digito4}{digito3}{digito6}{digito5}')