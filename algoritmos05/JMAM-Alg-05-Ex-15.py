def hex2int(valor):
    hexNums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','F']
    for index,numero in enumerate(hexNums):
        if numero == valor.upper():
            return index

def int2hex(valor):
    hexNums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','F']
    return hexNums[valor]

def main():    
    #teste
    print(hex2int('C'))
    print(int2hex(12))

if __name__ == '__main__':
    main()
