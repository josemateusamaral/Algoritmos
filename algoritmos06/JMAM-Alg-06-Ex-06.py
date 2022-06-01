def divisores(numero):
    divisores = []
    for divisor in range(1,numero):
        if numero % divisor == 0:
            divisores.append(divisor)
    return divisores

def main():
    numero = int(input('Digite um número inteiro: '))
    print(f'\nSeu número é: {numero}\n\nOs divisores são: ')
    print(divisores(numero))

if __name__ == '__main__':
    main()
