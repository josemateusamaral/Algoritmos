def strip(string):
    novaString = ''
    for caractere in string:
        if caractere != ' ':
            novaString += caractere
    return novaString

def tokenise(string):
    numero = ''
    token = []
    for index,char in enumerate(string):

        if char in ['/','*','^','(',')','=']:
            if numero != '':
                token.append(int(numero))
            numero = ''
            token.append(char)

        elif char in ['-','+']:
            if string[index-1] in '0987654321)' and index != 0:
                if numero != '':
                    token.append(int(numero))
                numero = ''
                token.append(char)
            else:
                numero += char

        elif char in '0987654321':
            numero += char
            if index + 1 == len(string):
                if numero != '':
                    token.append(int(numero))

    return token

def main():
    expressao = input('Digite uma expressão para ser tokenisada\n:')
    expressaoFormatada = strip(expressao)
    print('\n\n[TOKEN]>',tokenise(expressaoFormatada))

if __name__ == '__main__':
    main()
