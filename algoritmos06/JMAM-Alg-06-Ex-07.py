def divisores(numero):
    divisores = []
    for divisor in range(1,numero):
        if numero % divisor == 0:
            divisores.append(divisor)
    return divisores

def isPerfeito(numero):
    divis = divisores(numero)
    somaDosDivisores = 0
    for divisor in divis:
        somaDosDivisores += divisor
    if somaDosDivisores == numero:
        return True
    else:
        return False

def main():
    for numero in range(1,10001):
        if isPerfeito(numero):
            print(numero)

if __name__ == '__main__':
    main()
