def getRaiz( numero, estimativa = 1.0 ):
    if estimativa == 1.0:
        raiz = numero / 2
    else:
        raiz = estimativa
    raiz = ( raiz + ( numero / raiz ) ) / 2
    if ( ( raiz ** 2 ) - numero ) < ( 10E-12 ):
        return raiz
    else:
        return getRaiz( estimativa = raiz , numero = numero )

def main():
    while True:
        numero = input('\n\n\nDigite um número para calcular sua raiz [ENTER para sair]:')
        if numero == '':
            break
        print(f'A raiz de {numero} é aproximadamente',getRaiz(int(numero)))
    print('[programa finalizado]')

if __name__ == '__main__':
    main()
