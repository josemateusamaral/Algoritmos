def descompactar( listaCompactada, listaDescompactada = [] ):
    if listaCompactada == []:
        return listaDescompactada
    for i in range(listaCompactada[1]):
        listaDescompactada.append(listaCompactada[0])
    return descompactar(listaCompactada[2:],listaDescompactada)

def main():
    listaCompactada = ['A',1,'B',5,'A',1,'B',1]
    print('\n\nLista descompactada:',descompactar(listaCompactada))
    print('\n\n[programa finalizado]')

if __name__ == '__main__':
    main()
