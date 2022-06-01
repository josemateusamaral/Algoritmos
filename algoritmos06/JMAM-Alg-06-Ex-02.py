def main():
    lista = []
    menor = None
    while True:
        numero = int(input('Digite um número [0 para sair]: '))
        if numero == 0:
            break
        for index,n in enumerate(lista):
            if n < numero:
                lista.insert(index,numero)
                break
        else:
            lista.append(numero)
    print('\n\n')
    for numero in lista:
        print(numero)

if __name__ == '__main__':
    main()
