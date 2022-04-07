numero = int(input('Digite um número inteiro de 3 dígitos: '))
digito1 = int(numero % 10)
digito2 = int((numero % 100) - digito1) // 10
digito3 = int((numero % 1000) - digito2) // 100
print(f'\n\nO número foi: {numero}\nO inverso é: {digito1}{digito2}{digito3}')