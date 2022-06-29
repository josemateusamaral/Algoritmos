def lerValor():
    numero = input('Digite um número para adicionar a soma [ENTER para sair]: ')
    if numero == '':
        return 0
    return lerValor() + float(numero)
    

def main():
    print('A soma dos valores digitados é',lerValor())
    print('[programa finalizado]')

if __name__ == '__main__':
    main()
