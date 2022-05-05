x = int(input('Digite um número para saber sua raiz: '))
raiz = x / 2
while True:
    raiz = ( raiz + ( x / raiz ) ) / 2
    if ( ( raiz ** 2 ) - x ) < ( 10E-12 ): break
print(f'A raiz de {x} é igual a {raiz}')
