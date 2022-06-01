def lista2string(lista):
    string = ''
    for index,palavra in enumerate(lista):
        if index == len(lista) - 1 and len(lista) > 1:
            string += ' e '
        elif len(lista) > 1 and index != 0:
            string += ', '
        string += palavra
    return string

def main():
    lista = []
    while True:
        palavra = input('Digite uma palavra para adicionar a sua lista [ENTER PARA SAIR]: ')
        if palavra == '': break
        lista.append(palavra)

    print('\n\nA sua lista é:\n',lista)
    print('\n\nA sua lista em formato de string é:\n',lista2string(lista))

if __name__ == '__main__':
    main()
