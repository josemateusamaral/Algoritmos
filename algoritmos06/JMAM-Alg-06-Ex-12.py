def isEmOrdem(lista):
    if len(lista) < 2:
        return True
    ultimoNumero = lista[0]
    for numero in lista:
        if numero < ultimoNumero:
            return False 
        ultimoNumero = numero
    return True

def main():
    lista = []
    while True:
        numero = input('Digite um número para adicionar a lista [ENTER PARA SAIR]: ')
        if numero == '': break
        lista.append(int(numero))
    print('\n\nSua lista de números é:\n',lista)
    if isEmOrdem(lista):
        print('\nSua lista está em ordem')
    else:
        print('\nSua lista não está em ordem')

if __name__ == '__main__':
    main()
