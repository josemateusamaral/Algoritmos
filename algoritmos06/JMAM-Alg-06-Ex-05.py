def main():
    numeros = []
    while True:
        numero = input('Digite um número inteiro: ')
        if numero == '':
            break
        else:
            numeros.append(int(numero))

    #negativos
    for numero in numeros:
        if numero < 0:
            print(numero,end=',')

    #zeros
    for numero in numeros:
        if numero == 0:
            print(numero,end=',')

    #positivos
    for numero in numeros:
        if numero > 0:
            print(numero,end=',')

if __name__ == '__main__':
    main()
    print()
