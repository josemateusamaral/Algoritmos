def areAnagramas(frase1,frase2):
    if len(frase1) != len(frase2):
        return False
    for caractere in frase1: 
        if caractere not in frase2:
            return False
    return True

def main():
    while True:
        palavras = input('\n\nDigite duas palavras para saber se são anagramas. Separe as palavras usando um espaço. Exemplo: roma amor.\n[ENTER para sair]: ')
        if palavras == '': break

        dados = palavras.split(' ')
        if areAnagramas(dados[0],dados[1]):
            print(f'\nAs palavras {dados[0]} e {dados[1]} são anagramas.')
        else:
            print(f'\nAs palavras {dados[0]} e {dados[1]} não são anagramas.')

    print('\n\n[programa finalizado]')

if __name__ == '__main__':
    main()