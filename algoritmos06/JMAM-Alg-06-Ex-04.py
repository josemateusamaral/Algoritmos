def main():
    palavras = []
    while True:
        palavra = input('Digite uma palavra para adicionar a lista [ENTER PARA SAIR]: ')
        if palavra == '':
            break
        else:
            if palavra not in palavras:
                palavras.append(palavra)

    for palavra in palavras:
        print(palavra)

if __name__ == '__main__':
    main()
