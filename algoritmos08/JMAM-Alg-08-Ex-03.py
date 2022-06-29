def isPalindromo(frase):
    if len(frase) < 2:
        return True
    if frase[0] != frase[-1]:
        return False
    return isPalindromo(frase[1:-1])

def main():
    while True:
        frase = input('\n\n\nDigite uma frase para saber se ela é um palíndromo [ENTER para sair]: ')
        if frase == '':
            break
        formatada = ''
        for caractere in frase:
            if caractere != ' ':
                formatada += caractere
        if isPalindromo(formatada):
            print(f'A frase "{frase}" é um palindromo')
        else:
            print(f'A frase "{frase}" não é um palindromo')
    print('[programa finalizado]')

if __name__ == '__main__':
    main()
