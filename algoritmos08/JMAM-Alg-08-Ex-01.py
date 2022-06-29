def fatorial(numero):
    if numero <= 1:
        return numero
    return numero * fatorial( numero - 1 )

def main():
    while True:
        numero = input('\n\n\nDigite um número para saber seu fatorial [ENTER para sair]: ')
        if numero == '':
            break
        print(f'O fatorial de {numero} é',fatorial(int(numero)))
    print('[programa finalizado]')

if __name__ == '__main__':
    main()
