numero = int(input('Digite um número inteiro de 3 dígitos: '))
digito1 = int(numero % 10)
digito2 = int((numero % 100) - digito1) // 10
digito3 = int((numero % 1000) - digito2) // 100
print(f'O dígito número foi: {numero}\nA centena é: {digito3}\nA dezena é: {digito2}\nA unidade é: {digito1}')