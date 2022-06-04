MORSE = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}

def converterParaMorse(frase):
    morse = ''
    for caractere in frase:
        if caractere.lower() not in MORSE:
            continue
        morse += ' ' + MORSE[caractere.lower()]
    return morse

def main():
    while True:
        frase = input('\n\nDigite uma frase para converte-ĺa para código morse [ENTER para sair]: ')
        if frase == '': break
        print(f'\n\nfrase original: {frase}\nfrase em morse: {converterParaMorse(frase)}')
    print('\n\n[programa finalizado]')

if __name__ == '__main__':
    main()