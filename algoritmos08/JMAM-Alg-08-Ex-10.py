def compactar( listaDescompactada, listaCompactada = [] ):
    if listaDescompactada == []:
        return listaCompactada
    listaCompactada.append(listaDescompactada[0])

    numeroDeRepeticoes = 0
    for index,cada in enumerate(listaDescompactada):
        if cada != listaDescompactada[0]:
            numeroDeRepeticoes = index
            break
    else:
        numeroDeRepeticoes = len(listaDescompactada)
    
    listaCompactada.append(numeroDeRepeticoes)
    return compactar(listaDescompactada[numeroDeRepeticoes:],listaCompactada)

def main():
    listaDescompactada = ["A","A","A","A","A","A","A","A","A","A","A","A","A","B","B","B","B","A","A","A","A","A","A","A","B","B","B","C"]
    print('\n\nLista compactada:',compactar(listaDescompactada))
    print('\n\n[programa finalizado]')

if __name__ == '__main__':
    main()
