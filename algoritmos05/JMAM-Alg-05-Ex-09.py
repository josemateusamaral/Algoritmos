def isInteger(string):
    striped = string.strip()
    for index,character in enumerate(striped):
        if (character in ['-','+']):
            if index > 0:
                return False
        elif (character not in ['0','1','2','3','4','5','6','7','8','9']):
            return False
    return True

def main():
    string = input('Digite uma string para saber se está string representa um número válido: ')
    if isInteger(string):
        print(f"A string '{string}' representa o número inteiro {string}")
    else:
        print(f"A string '{string}' não representa um número inteiro válido")

if __name__ == '__main__':
    main()
