import random

def gerarSenhaAleatoria():
    opcaoComprimento = range(7,11)
    comprimento = random.choice(opcaoComprimento)
    opcoes = range(33,127)
    senha = ''
    for digito in range(comprimento):
        senha += chr(random.choice(opcoes))
    return senha

def main():
    print('A sua senha aleatória é: ',gerarSenhaAleatoria())

if __name__ == '__main__':
    main()
