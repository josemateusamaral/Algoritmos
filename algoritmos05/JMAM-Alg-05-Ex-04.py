def mediana(a,b,c):
    mediana = ( a + b + c) - ( min(a,b,c) + max(a,b,c) ) 
    return mediana

def main():
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    c = float(input('Digite o terceiro número: '))
    media = mediana(a,b,c)
    print(f'O mediana de {a}, {b} e {c} é igual a {media}')

if __name__ == '__main__':
    main()
