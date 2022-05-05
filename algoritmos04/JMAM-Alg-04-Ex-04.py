from math import sqrt

quantidadeDeVertices = 1
perimetro = 0
stringX = 'Digite a coordenada x de um ponto:'
stringY = 'Digite a coordenada y de um ponto:'

xInicial = int(input('Digite a coordenada x de um ponto:'))
yInicial = int(input('Digite a coordenada y de um ponto:'))
ultimoX = xInicial
ultimoY = yInicial
end = False

while True:
    quantidadeDeVertices += 1
    xAtual = input('Digite a coordenada x de um ponto:(enter para sair):')
    if xAtual == '':
        xAtual = xInicial
        yAtual = yInicial
        end = True
    else:
        yAtual = int(input('Digite a coordenada y de um ponto:'))

    x = ( int(xAtual) - ultimoX ) ** 2
    y = ( yAtual - ultimoY ) ** 2
    perimetro += sqrt( x + y )
    ultimoX = int(xAtual)
    ultimoY = yAtual
    
    if end: break
    
print('O perimetro deste poligono é igual a ',perimetro)
