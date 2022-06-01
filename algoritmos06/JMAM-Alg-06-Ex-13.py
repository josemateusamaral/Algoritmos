def countRange(lista,maximo,minimo):
    quantidade = 0
    for numero in lista:
        if numero >= minimo and numero < maximo:
            quantidade += 1
    return quantidade

def main():
    listaDeNumeros = []
    while True:
        numero = input('Digite um número para adicionar a lista [ENTER PARA SAIR]: ')
        if numero == '': break
        listaDeNumeros.append(float(numero))

    maximo = float(input('Digite um número para ser seu número maximo: '))
    minimo = float(input('Digite um número para ser seu número minimo: '))

    print(f'\n\nA quantidade de números maiores ou iguais a {minimo} e menores que {maximo} é:',countRange(listaDeNumeros,maximo,minimo))

if __name__ == '__main__':
    main()
