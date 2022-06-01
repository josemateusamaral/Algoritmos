def getPrecedencia(string):
    if string in ['+','-']: return 1
    elif string in ['*','/']: return 2
    elif string in ['^']: return 3
    else: return -1

def main():
    while True:
        operador = input('\n\nDigite um operador para saber sua precedencia [ENTER PARA SAIR]: ')
        precedencia = getPrecedencia(operador)
        if precedencia == -1:
            print('Você não digitou um operador válido')
        else:
            print(f'A precedencia do operador {operador} é',precedencia)
        input('\n[ENTER] para continuar')

if __name__ == '__main__':
    main()
