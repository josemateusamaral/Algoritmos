def main():
    listaDeNumeros = []
    while True:
        numero = int(input('Digte um número inteiro [0 para sair]: '))
        if numero == 0:
            break
        else:
            listaDeNumeros.append(numero)
            
    for numero in sorted(listaDeNumeros):
        print(numero)

if __name__ == '__main__':
    main()

