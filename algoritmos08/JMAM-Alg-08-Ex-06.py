def getMDC(a,b):
    if b == 0:
        return a
    else:
        c = a % b
        return getMDC(b,c)

def main():
    while True:
        a = input('\n\n\nDigite o primeiro número [ENTER para sair]: ')
        if a == '':
            break
        b = input('Digite o segundo número: ')
        print(f'O MDC dos números {a} e {b} é',getMDC(int(a),int(b)))
    print('[programa finalizado]')

if __name__ == '__main__':
    main()
