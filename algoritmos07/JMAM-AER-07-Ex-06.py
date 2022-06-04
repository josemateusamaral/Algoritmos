def areAnagramas(frase1,frase2):
    frase1 = frase1.replace(' ','').lower()
    frase2 = frase2.replace(' ','').lower()
    if len(frase1) != len(frase2):
        return False
    for caractere in frase1: 
        if caractere not in frase2:
            return False
    return True

def main():
    frase1 = input('\n\nDigite a primeira frase: ')
    frase2 = input('\n\nDigite a segunda frase: ')
    if areAnagramas(frase1,frase2):
        print(f'\nAs frases {frase1} e {frase2} são anagramas.')
    else:
        print(f'\nAs frases {frase1} e {frase2} não são anagramas.')

if __name__ == '__main__':
    main()