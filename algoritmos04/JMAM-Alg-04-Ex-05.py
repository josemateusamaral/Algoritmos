soma = 0
while True:
    idade = input('Entre uma idade: ')
    if idade == '': break

    idade = int(idade)
    if idade <= 2: soma += 0
    elif idade <= 12: soma += 14
    elif idade <= 65: soma += 18
    else: soma += 23

print(f'A soma do valor do ingresso de todas as pessoas foi R${soma}')
