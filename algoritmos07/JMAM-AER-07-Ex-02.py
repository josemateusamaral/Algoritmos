def main():
    m = set()
    n = set()
    while True:
        numero = input(f'\n\n\nDigite um número inteiro para adiciona-lo ao conjunto M:{m}\n(ENTER para sair): ')
        if numero == '':
            break
        m.add(int(numero))

    while True:
        numero = input(f'\n\n\nDigite um número inteiro para adiciona-lo ao conjunto N:{n}\n(ENTER para sair): ')
        if numero == '':
            break
        n.add(int(numero))
    
    diferencaSimetrica = []
    for numero in m:
        if numero not in n:
            diferencaSimetrica.append(numero)
    for numero in n:
        if numero not in m:
            diferencaSimetrica.append(numero)

    print(f'\n\nA diferença simetrica entre os conjuntos  m:{m} e n:{n} é {diferencaSimetrica}')

if __name__ == '__main__':
    main()