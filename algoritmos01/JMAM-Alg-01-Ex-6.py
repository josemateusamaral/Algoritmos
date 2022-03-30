soma = float(input('Digite o valor do suco: ')) + float(input('Digite o valor do prato principal: ')) + float(input('Digite o valor da sobremesa: '))
servico = (soma / 100) * 10
print('O preço da refeição foi: R$ {:.2f}'.format(soma + servico))