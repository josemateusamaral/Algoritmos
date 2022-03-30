from math import sqrt
l1 = float(input('Informe o comprimento do lado 1 do triângulo: '))
l2 = float(input('Informe o comprimento do lado 2 do triângulo: '))
l3 = float(input('Informe o comprimento do lado 3 do triângulo: '))
l = (l1 + l2 + l3) / 2
print('A área do triângulo é: ' + str(sqrt(l * (l - l1) * (l - l2) * (l - l3))))