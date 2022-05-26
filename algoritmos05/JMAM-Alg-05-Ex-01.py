from math import sqrt

def calcularHipotenusa(lado1,lado2):
    hipotenusa = sqrt( (lado1**2) + (lado2**2) )
    return hipotenusa

def main():
    lado1 = float(input('Digite o primeiro lado do triângulo retângulo: '))
    lado2 = float(input('Digite o segundo lado do triângulo retângulo: '))
    hipotenusa = calcularHipotenusa(lado1,lado2)
    print(f'A hipotenusa de um triângulo retângulo com os lados de comprimento {lado1} e {lado2} é {hipotenusa}')

if __name__ == '__main__':
    main()
