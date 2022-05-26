def isPrimo(numero):
    for n in range(2,numero+1):
        if numero % n == 0 and n != numero: return False
    return True

def main():
    numero = int(input('Digite um número inteiro positivo para saber se este número é um número primo: '))
    if isPrimo(numero):
        print(f"O número {numero} é um número primo")
    else:
        print(f"O número {numero} não é um número primo")

if __name__ == '__main__':
    main()
