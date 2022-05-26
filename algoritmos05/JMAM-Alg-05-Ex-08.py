def formatarString(string):
    up = True
    novaString = ''
    for caractere in string:
        if caractere in ['.','!','?']:
            novaString += caractere
            up = True
            continue
        if up and caractere != ' ':
            novaString += caractere.upper()
            up = False
        else:
            novaString += caractere
    return novaString

def main():
    string = input('Digite uma string para que ela sejá formatada para o uso correto de letras maiusculas: ')
    print(formatarString(string))

if __name__ == '__main__':
    main()
