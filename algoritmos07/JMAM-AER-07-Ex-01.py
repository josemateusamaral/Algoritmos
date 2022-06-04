def temUnicos(string):
    conjunto = set(list(string))
    if len(conjunto) == len(string):
        return True
    else:
        return False

def main():
    while True:
        string = input('\n\n\nDigite uma string para saber se esta string possui apenas caracter unicos\n(ENTER para sair): ')
        if string == '':
            break
        if temUnicos(string):
            print(f"A palavra '{string}' não possui caracteres repetidos")
        else:
            print(f"A palavra '{string}' possui caracteres repetidos")

    print('\n\n[programa finalizado]')

if __name__ == '__main__':
    main()