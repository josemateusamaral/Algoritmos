def main():
    frase = input('Digite uma frase para obter sua lista de palavras: ')
    palavras = []
    ultimaPalavra = ''
    for index,letra in enumerate(frase):

        if letra != ' ' and letra.lower() in 'abcdefghijklmnopqrstuvwxyzç':
            ultimaPalavra += letra
        elif letra == ' ' and ultimaPalavra != '': 
            palavras.append(ultimaPalavra)
            ultimaPalavra = ''
        
        if index == len(frase) - 1 and ultimaPalavra != '':
            palavras.append(ultimaPalavra)

    print('Sua lista de palavras é :\n',palavras)

if __name__ == '__main__':
    main()
