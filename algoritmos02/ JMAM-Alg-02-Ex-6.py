numero = int(input('Digite um número inteiro de 4 digitos: '))
digito1 = int(numero % 10)
digito2 = int((numero % 100) - digito1) // 10
digito3 = int((numero % 1000) - digito2) // 100
digito4 = int((numero % 10000) - digito3) // 1000 
soma = digito1 + digito2 + digito3 + digito4
print(f'\n\n\nNúmero inteiro foi: {numero}\nA soma dos dígitos [{digito4},{digito3},{digito2},{digito1}] é: {soma}')