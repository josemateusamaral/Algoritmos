def main():
    lista = []
    while True:
        numero = int(input('Digite um número inteiro [0 para sair]: '))
        if numero == 0:
            if len(lista) < 4:
                print('Sua lista de números deve ter ao menos 4 numeros !!')
                input('[ENTER] para continuar')
            else: break
        lista.append(numero)
    novaLista = []
    for numero in lista: novaLista.append(numero)

    #tirar os dois maiores
    for i in range(2):
        maior = novaLista[0]
        for numero in novaLista:
            if numero > maior: maior = numero
        novaLista.remove(maior)

    #tirar os dois menores
    for i in range(2):
        menor = lista[0]
        for numero in novaLista:
            if numero < menor: menor = numero
        novaLista.remove(menor)

    print('\nNova lista sem os 2 maiores e os 2 menores\n',novaLista)
    print('\nLista original\n',lista)

if __name__ == '__main__':
    main()
    
