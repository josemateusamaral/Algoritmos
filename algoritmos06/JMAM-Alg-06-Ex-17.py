def strip(string):
    novaString = ''
    for caractere in string:
        if caractere != ' ':
            novaString += caractere
    return novaString

def precedencia(string):
    if string in ['+','-']: return 1
    elif string in ['*','/']: return 2
    elif string in ['^']: return 3
    else: return -1

def tokeniseINFIXA(string):
    numero = ''
    token = []
    for index,char in enumerate(string):

        if char in ['/','*','^','(',')','=']:
            if numero != '':
                token.append(int(numero))
            numero = ''
            token.append(char)

        elif char in ['-','+']:
            if string[index-1] in '0987654321)+-':
                if numero != '':
                    token.append(int(numero))
                    numero = ''
                token.append(char)
            else:
                numero += char

        elif char in '0987654321':
            numero += char
            if index + 1 == len(string):
                if numero != '':
                    token.append(int(numero))
    return token

def tokenisePOSFIXA(token):
    posFixa = []
    operadores = []
    for index,tkn in enumerate(token):
        if isinstance(tkn,int):
            posFixa.append(tkn)
            
        if str(tkn) in '+-*/^':
            while operadores != [] and operadores[-1] != '(' and precedencia(tkn) <= precedencia(operadores[-1]):
                posFixa.append(operadores.pop(-1))
            operadores.append(tkn)

        if str(tkn) == '(':
            operadores.append(tkn)

        if str(tkn) == ')':
            while operadores[-1] != '(':
                posFixa.append(operadores.pop(-1))
            operadores.remove('(')

    while operadores != []:
        posFixa.append(operadores.pop(-1))
        
    return posFixa

def valorDaExpressao(token):
    valores = []
    for tkn in token:
        if str(tkn) not in '-+/*^':
            valores.append(tkn)
        else:
            direita = valores.pop(-1)   
            esquerda = valores.pop(-1)
            if tkn == '*':
                valores.append( esquerda * direita )
            if tkn == '+':
                valores.append( esquerda + direita )
            if tkn == '-':
                valores.append( esquerda - direita )
            if tkn == '/':
                valores.append( esquerda / direita )
            if tkn == '^':
                valores.append( esquerda ** direita )
    return valores[0]

def main():
    expressao = input('Digite uma expressão para ser tokenisada na forma posFixada e na forma inFixada\n: ')
    expressaoFormatada = strip(expressao)
    infixa = tokeniseINFIXA(expressaoFormatada)
    posfixa = tokenisePOSFIXA(infixa)
    valor = valorDaExpressao(posfixa)
    
    print('\n\n[TOKEN INFIXA]>',infixa)
    print('\n\n[TOKEN POSFIXA]>',posfixa)
    print('\n\n[VALOR]>',valor)

if __name__ == '__main__':
    main()
