def trianguloValido(a,b,c):
    if a > b + c or b > a + c or c > a + b:
        return False
    return True

def main():
    a = float(input('Digite o valor do primeiro lado do triângulo: '))
    b = float(input('Digite o valor do segundo lado do triângulo: '))
    c = float(input('Digite o valor do terceiro lado do triângulo: '))
    if trianguloValido(a,b,c):
        print(f'Usando os comprimentos {a}, {b} e {c} é possivel formar um triângulo')
    else:
        print(f'Usando os comprimentos {a}, {b} e {c} não é possivel formar um triângulo')

if __name__ == '__main__':
    main()
