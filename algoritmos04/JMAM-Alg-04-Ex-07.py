for quantidadeDeAproximacoes in range(1,16):
    pi = 3
    for aproximacao in range(1,quantidadeDeAproximacoes):
        multiplicadorInicial = aproximacao * 2
        ap = 4 / ( multiplicadorInicial * (multiplicadorInicial + 1) * (multiplicadorInicial + 2) )
        if aproximacao % 2 == 0: pi -= ap
        else: pi += ap
    print(pi)
