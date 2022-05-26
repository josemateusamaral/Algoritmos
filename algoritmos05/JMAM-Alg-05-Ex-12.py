def isValide(senha):
    if len(senha) < 8: 
        return False
    temMaiuscula = False
    temMinuscula = False
    temNumero = False
    for caractere in senha:
        if caractere.islower():
            temMinuscula = True
        if caractere.isupper():
            temMaiuscula = True
        if caractere in ['1','2','3','4','5','6','7','8','9','0']:
            temNumero = True
    if temNumero and temMaiuscula and temMinuscula:
        return True
    else:
        return False

def main():
    senha = input('Digite uma senha para verificar se esta senha é válida: ')
    if isValide(senha):
        print(f"A senha '{senha}' é uma senha válida")
    else:
        print(f"A senha '{senha}' nao é uma senha válida")

if __name__ == '__main__':
    main()
