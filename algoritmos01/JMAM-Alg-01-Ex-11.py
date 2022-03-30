from math import radians,sin,cos,acos
latitude1 = radians(float(input('Informe a latitude do ponto1 em graus: ')))
longitude1 = radians(float(input('Informe a longitude do ponto1 em graus: ')))
latitude2 = radians(float(input('Informe a latitude do ponto2 em graus: ')))
longitude2 = radians(float(input('Informe a longitude do ponto2 em graus: ')))
print('A distância entre os dois pontos é: ' + str(6371.01 * acos(sin(latitude1) * sin(latitude2) + cos(latitude1) * cos(latitude2) * cos(longitude1 - longitude2))))