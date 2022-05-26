def calcularFrete(quantidadeDeProdutos):
    valorDoFrete = 0
    for produto in range(quantidadeDeProdutos):
        if valorDoFrete == 0:
            valorDoFrete += 10.95
        else:
            valorDoFrete += 2.95
    return valorDoFrete

def main():
    quantidadeDeProdutos = int(input('Digite a quantidade de produtos para saber o valor do frete: '))
    valorDoFrete = calcularFrete(quantidadeDeProdutos)
    print(f'O valor do frete para enviar {quantidadeDeProdutos} é igual a R$ {valorDoFrete:.2f}')

if __name__ == '__main__':
    main()
