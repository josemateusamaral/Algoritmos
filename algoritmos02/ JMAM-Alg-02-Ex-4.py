import random
primeiroNumero = int(input('Digite o primeiro númeor inteiro: '))
segundoNumero = int(input('Digite o segundo número inteiro: '))
terceiroNumero = int(input('Digite o terceiro número inteiro: '))
menor = min(primeiroNumero,segundoNumero,terceiroNumero)
maior = max(primeiroNumero,segundoNumero,terceiroNumero)
meio = (primeiroNumero+segundoNumero+terceiroNumero)-menor-maior
print(f'{menor}\n{meio}\n{maior}')