import random

def main():
    numerosDaSena = []
    opcoesDeNumeros = range(1,61)
    while len(numerosDaSena) < 6:
        numero = random.choice(opcoesDeNumeros)
        if numero not in numerosDaSena:
            numerosDaSena.append(numero)
            
    print('\n\nSeus numeros da mega-sena são')
    for numero in sorted(numerosDaSena):
        print(numero,end=' ')

if __name__ == '__main__':
    main()
    print()
