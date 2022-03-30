from math import tan,pi
l = float(input('Informe o comprimento dos lados do polígono: '))
n = int(input('Informe o número de lados do polígono: '))
print('A área do polígono é: ' + str((n * (l ** 2)) / (4 * tan(pi / n))))