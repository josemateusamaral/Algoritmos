def getChaves(dicionario,valor):
    chaves = []
    for chave in dicionario:
        if dicionario[chave] == valor:
            chaves.append(chave)
    return chaves

def main():
    dicionario = {}
    while True:
        adicionar = input('\n\nDigite uma chave e um valor para adicionar ao seu dicionario.\nSepare a chave e o valor usando uma virgula.\nExemplo. digite "banana,amarela" para adicionar o valor amarela a chave banana (ENTER para sair): ')
        if adicionar == '':
            break
        dados = adicionar.split(',')
        dicionario[dados[0]] = dados[1]
    
    procurar = input('\n\nDigite um valor para encontrar todas as chaves que tem este valor: ')
    print(f"\n\nAs chaves que contem o valor '{procurar}' são {getChaves(dicionario,procurar)}")

    print('\n\n[programa finalizado]')

if __name__ == '__main__':
    main()