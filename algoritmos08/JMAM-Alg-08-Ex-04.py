numeros_de_fibonacci = [0,1]
def fibonacci(numero):
    if len(numeros_de_fibonacci) >= numero:
        return numeros_de_fibonacci[-1]
    numeros_de_fibonacci.append(numeros_de_fibonacci[-1] + numeros_de_fibonacci[-2])
    return fibonacci(int(numero))

def main():
    while True:
        numero = input('\n\n\nDigite um número para achar o número de fibonacci correspondente a esta posição [ENTER para sair]: ')
        if numero == '':
            break
        print(f'O número {numero} de fibonacci é',fibonacci(int(numero)))
    print('[programa finalizado]')

if __name__ == '__main__':
    main()
