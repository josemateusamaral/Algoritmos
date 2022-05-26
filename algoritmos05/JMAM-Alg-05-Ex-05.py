def acharOrdinario(numero):
    ordinarios = ['primeiro','segundo','terceiro','quarto','quinto','sexto','sétimo','oitavo','nono','décimo','décimo-primeiro','décimo-segundo']
    if numero < 1 and numero > 12:
        return ''
    return ordinarios[numero-1]

def main():
    for numero in range(1,13):
        ordinario = acharOrdinario(numero)
        print(f'{numero}\t{ordinario}')
    numero = int(input('Digite um número para saber seu ordinário: '))
    ordinario = acharOrdinario(numero)
    print(f'O ordinario do número {numero} é igual a {ordinario}')

if __name__ == '__main__':
    main()
