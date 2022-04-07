dias = int(input('numero de dias:')) * 24 * 60 * 60
horas = int(input('numero de horas:')) * 60 * 60
minutos = int(input('numero de minutos:')) * 60
segundos = int(input('numero de segundos:'))
quantidadeSegundos = dias + horas + minutos + segundos
print(f'A quantidade de segundos é: {quantidadeSegundos}')