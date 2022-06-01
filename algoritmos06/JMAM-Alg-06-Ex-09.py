def main():
    notas = []
    while True:
        nota = input('Digite uma nota: ')
        if nota == '': break
        notas.append(float(nota))

    somaDaNotas = 0
    quantidadeDeNotas = len(notas)
    for nota in notas:
        somaDaNotas += nota
    media = round(somaDaNotas / quantidadeDeNotas,2)
    
    naMedia = []
    abaixoDaMedia = []
    acimaDaMedia = []
    for nota in notas:
        if nota == media:
            naMedia.append(nota)
        elif nota < media:
            abaixoDaMedia.append(nota)
        elif nota > media:
            acimaDaMedia.append(nota)
    
    print(f'\nA média das notas é\n{media}')
    print(f'\nNotas na média\n{naMedia}')
    print(f'\nNotas abaixo da média\n{abaixoDaMedia}')
    print(f'\nNotas acima da média\n{acimaDaMedia}')

    

if __name__ == '__main__':
    main()
