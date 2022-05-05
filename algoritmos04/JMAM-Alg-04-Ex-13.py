numero = int(input('Digite uma número inteiro para obter sua fatoração: '))
fator = 2
while numero != 1:
    if numero % fator == 0:
        numero = numero / fator
        print(fator)
    else: fator += 1
