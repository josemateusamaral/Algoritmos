def isMagic(dia,mes,ano):
    if str(dia * mes) == str(ano)[2:]:
        return True
    else:
        return False

def getDays(mes,ano):
    fevereiro = 28
    if (ano % 400 == 0 and ano % 4 == 0 and ano % 100 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        fevereiro = 29
    diasPorMes = [31,fevereiro,31,30,31,30,31,31,30,31,30,31]
    return diasPorMes[mes-1]

def main():
    for ano in range(1901,2001):
        for mes in range(12):
            for dia in  range(getDays(mes+1,ano)):
                if isMagic(dia,mes,ano):
                    print(f'{dia}\{mes}\{ano} é uma data mágica')

if __name__ == '__main__':
    main()
