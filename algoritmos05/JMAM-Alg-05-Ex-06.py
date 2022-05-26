def centralizarString(string,larguraLinha):
    newString = ''
    larguraString = len(string)
    quantidadeDeEspacoesNoComeco = int( ( larguraLinha / 2 ) - ( int(larguraString) / 2 ) )
    for i in range(quantidadeDeEspacoesNoComeco):
        newString += ' '
    newString += string
    return newString

def main():
    string = input('Digite uma string para centraliza-la no terminal: ')
    larguraLinha = int(input('Digite a largura do terminal em caracteres: '))
    print('\n',centralizarString(string,larguraLinha))

if __name__ == '__main__':
    main()
