def getDays(mes,ano):
    fevereiro = 28
    if (ano % 400 == 0 and ano % 4 == 0 and ano % 100 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        fevereiro = 29
    diasPorMes = [31,fevereiro,31,30,31,30,31,31,30,31,30,31]
    return diasPorMes[mes-1]

def main():
    mes = int(input('Digite um mês entre 1 e 12: '))
    ano = int(input('Digite um ano: '))
    print(f"A quantidade de dias no mês {mes} do ano {ano} é igual a",getDays(mes,ano))

if __name__ == '__main__':
    main()
