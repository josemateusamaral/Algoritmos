DISTANCIA_DA_TARIFA = 140
TARIFA = 0.25
VALOR_INICIAL = 4

def calcularPreco(distancia):
    valorDaCorrida = ( ( distancia / DISTANCIA_DA_TARIFA ) * TARIFA ) + VALOR_INICIAL
    return valorDaCorrida

def main():
    distanciaPercorrida = float(input('Digite a distância percorrida pelo taxi: '))
    valorDaCorrida = calcularPreco(distanciaPercorrida)
    print(f'Para percorrer a distância de {distanciaPercorrida} metros o valor da corrida fica em R$ {valorDaCorrida:.2f}')

if __name__ == '__main__':
    main()
