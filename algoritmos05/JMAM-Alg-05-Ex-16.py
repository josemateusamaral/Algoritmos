import os

def bin2int(binario):
    position = len(binario) - 1
    decimal = 0
    for digito in binario:
        valor = int(digito) * (2**position)
        decimal += int(valor)
        position -= 1
    return decimal

def int2bin(valor):
    valor = int(valor)
    binario = ''
    while valor != 0:
        resto = valor % 2
        if resto == 0:
            binario = '0' + binario
        else:
            binario = '1' + binario
        valor = valor // 2
    return binario

def hex2int(hexadecimal):
    hexNums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','F']
    position = len(hexadecimal) - 1
    decimal = 0
    for digito in hexadecimal:
        valor = int(hexNums.index(digito.upper())) * (16**position)
        decimal += int(valor)
        position -= 1
    return decimal

def int2hex(valor):
    hexNums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','F']
    valor = int(valor)
    hexadecimal = ''
    while True:
        resto = valor % 16
        hexadecimal = hexNums[resto] + hexadecimal
        valor = valor // 16
        if valor == 0:
            break
    return hexadecimal

def main():
    while True:
        os.system('cls')
        numero = input('Digite seu número para fazer a conversão [ENTER PARA SAIR]: ')
        baseDoNumero = int(input('Em que base seu número está [ 2 , 10 , 16 ]: '))
        if numero == '': break
        baseParaConverter = int(input('Para que base você quer converter esse número [ 2 , 10 , 16 ]: '))
        
        if baseParaConverter == 2:
            if baseDoNumero == 10:
                binario = int2bin(numero)
                print(f'\nO decimal "{numero}" em binário é igual a "{binario}"')
                input('\n\n[ENTER] para continuar')
            elif baseDoNumero == 16:
                decimal = hex2int(numero)
                binario = int2bin(decimal)
                print(f'\nO hexadecimal "{numero}" em binário é igual a "{binario}"')
                input('\n\n[ENTER] para continuar')

        elif baseParaConverter == 10:
            if baseDoNumero == 2:
                decimal = bin2int(numero)
                print(f'\nO binário "{numero}" em decimal é igual a "{decimal}"')
                input('\n[ENTER] para continuar')
            elif baseDoNumero == 16:
                decimal = hex2int(numero)
                print(f'\nO hexadecimal "{numero}" em decimal é igual a "{decimal}"')
                input('\n\n[ENTER] para continuar')
            

        elif baseParaConverter == 16:
            if baseDoNumero == 10:
                hexadecimal = int2hex(numero)
                print(f'\nO decimal "{numero}" em hexadecimal é igual a "{hexadecimal}"')
                input('\n[ENTER] para continuar')
            elif baseDoNumero == 2:
                decimal = bin2int(numero)
                hexadecimal = int2hex(decimal)
                print(f'\nO binário "{numero}" em hexadecimal é igual a "{hexadecimal}"')
                input('\n[ENTER] para continuar')
            

if __name__ == '__main__':
    main()








    
