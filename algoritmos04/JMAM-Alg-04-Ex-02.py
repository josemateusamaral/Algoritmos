print('Produto\t\tDesconto\tValor final')
for produto in [4.95,9.95,14.95,19.95,24.95]:
    desconto = produto * 0.6
    valorFinal = produto - desconto
    print(f'R${produto:.2f}\t\tR${desconto:.2f}\t\tR${valorFinal:.2f}')
