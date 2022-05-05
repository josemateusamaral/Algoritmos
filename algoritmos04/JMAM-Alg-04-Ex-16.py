from random import randint
somaDosSorteios = 0

for tentativa in range(10):
    ultimo = None
    sorteios = 0
    repeticoes = 0
    while True:
        
        resposta = randint(0,1)
        if resposta == ultimo: repeticoes += 1
        else:repeticoes = 0
        if repeticoes == 3: break

        ultimo = resposta
        sorteios += 1
        if resposta == 1: print('A',end=' ')
        else: print('0',end=' ')
        
    somaDosSorteios += sorteios
    print(f'({sorteios} sorteios)',end='\n')

media = somaDosSorteios / 10       
print(f'Na média, foram necessários {media} sorteios.')
    
