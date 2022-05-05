binario = input('\nDigite uma número binario para converter para decimal: ')
position = len(binario) - 1
decimal = 0
for digito in binario:
    valor = int(digito) * (2**position)
    decimal += int(valor)
    position -= 1
print('\nO número binário ',binario,' equivalo ao número decimal ',decimal)
