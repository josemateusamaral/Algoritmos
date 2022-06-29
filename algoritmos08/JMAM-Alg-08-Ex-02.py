def fibonacci(numero,numeros):
    if len(numeros) >= numero:
        return numeros[-1]
    numeros.append(numeros[-1] + numeros[-2])
    return fibonacci(int(numero),numeros)

def main():
    while True:
        numero = input('\n\n\nDigite um número para achar o número de fibonacci correspondente a esta posição [ENTER para sair]: ')
        if numero == '':
            break
        print(f'O número {numero} de fibonacci é',fibonacci(int(numero),[0,1]))
    print('[programa finalizado]')

if __name__ == '__main__':
    main()
