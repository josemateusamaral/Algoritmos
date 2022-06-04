import random
import os

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
    print('\n\n------------------------------------')
    for coluna in cartela:
        if coluna == 'B': 
            print('|',coluna,end='\t')
        elif coluna == 'O':
            print(coluna,' |',end='\t')
        else:
            print(coluna,end='\t')
    print('\n------------------------------------')  
    for linha in range(5):
        for coluna in cartela:
            if coluna == 'B': 
                print('|',cartela[coluna][linha],end='\t')
            elif coluna == 'O':
                if cartela[coluna][linha] < 10:
                    print(end=' ')
                print(cartela[coluna][linha],'|',end='\t')
            else:
                print(cartela[coluna][linha],end='\t')
        print()
    print('------------------------------------')  

def marcarCartela(cartela,sorteio):
    for coluna in cartela:
        for index,linha in enumerate(cartela[coluna]):
             if linha in sorteio:
                cartela[coluna][index] = 0
    return cartela

def verificarCartela(cartela,sorteio):
    #verificar verticais
    for coluna in cartela:
        soma = 0
        for linha in cartela[coluna]:
            soma += linha
        if soma == 0:
            return True
        
    #verificar horizontais
    for linha in range(5):
        soma = 0
        for coluna in cartela:
            soma += cartela[coluna][linha]
        if soma == 0:
            return True

    #verificar diagonais
    diagonais = [[0,1,2,3,4],[4,3,2,1,0]]
    for diagonal in diagonais:
        soma = 0
        for index,coluna in enumerate(cartela):
            soma += cartela[coluna][diagonal[index]]
        if soma == 0:
            return True
    
    return False

def sorteioInicial():
    numeros = range(1,76)
    sorteio = []
    for n in range(4):
        while True:
            numero = random.choice(numeros)
            if numero not in sorteio:
                sorteio.append(numero)
                break
    return sorteio

def main():

    maximo = 0
    minimo = 75
    soma = 0
    quantidadeDeJogos = 1000

    for vezes in range(quantidadeDeJogos):
        #inicializacao do jogo
        numeros = range(1,76)
        sorteio = sorteioInicial()
        cartela = generateCartela()
        
        while True:
            
            #sortear numero
            while True:
                numero = random.choice(numeros)
                if numero not in sorteio:
                    sorteio.append(numero)
                    break
            os.system('cls')

            #renderizar jogo
            print(vezes + 1,'de',quantidadeDeJogos)
            cartelaMarcada = marcarCartela(cartela,sorteio)
            renderCartela(cartelaMarcada)

            #verificar resultado
            verificacao = verificarCartela(cartelaMarcada,sorteio)
            if verificacao:
                quantidadeDeSorteios = len(sorteio)
                soma += quantidadeDeSorteios
                if quantidadeDeSorteios < minimo:
                    minimo = quantidadeDeSorteios
                if quantidadeDeSorteios > maximo:
                    maximo = quantidadeDeSorteios
                break

    print()
    media = round(soma / quantidadeDeJogos,2)
    print(f'Maximo: {maximo}\nMinimo: {minimo}\nMédia: {media}')
    print('\n\n[programa finalizado]\n')

if __name__ == '__main__':
    main()
