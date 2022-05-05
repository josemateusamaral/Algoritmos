soma = 0
quantidadeNotas = 0
while True:
    nota = input('Digite uma nota: ')
    if nota == '0' or nota == '': break
    soma += float(nota)
    quantidadeNotas += 1
media = soma / quantidadeNotas
print(f'A média das notas é {media:.2f}')
