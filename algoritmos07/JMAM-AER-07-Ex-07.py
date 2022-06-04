import random

def generateCartela():
    cartela = {}
    colunas = 'BINGO'
    opcoes = range(1,16)
    for index,coluna in enumerate(colunas):
        linhaInicial = index * 15
        linhas = []
        for linha in range(5):
            numero = None
            while True:
                numero = linhaInicial + random.choice(opcoes)
                if numero not in linhas:
                    break
            linhas.append(numero)
        cartela[coluna] = linhas
    return cartela

def renderCartela(cartela):
    for coluna in cartela:
        print(coluna,end='\t')
    print()
    for linha in range(5):
        for coluna in cartela:
            print(cartela[coluna][linha],end='\t')
        print()

def main():
    cartela = generateCartela()
    renderCartela(cartela)

if __name__ == '__main__':
    main()