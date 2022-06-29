def DecBinIterativo(q,result):
    if q == 0:
        return result
    r = q % 2
    result = str(r) + result
    q = q // 2
    return DecBinIterativo(int(q),result)

def main():
    while True:
        decimal = input('\n\n\nDigite um número decimal para converte-lo para binário [ENTER para sair]:')
        if decimal == '':
            break
        print(f'O decimal {decimal} em binário é',DecBinIterativo(int(decimal),''))
    print('[programa finalizado]')

if __name__ == '__main__':
    main()
