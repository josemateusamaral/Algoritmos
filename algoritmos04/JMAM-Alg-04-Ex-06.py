while True:
    bits = input('\nDigite uma sequencia de 8 bits: ')
    if bits == '': break

    if bits.count('1') + bits.count('0') < len(bits) or len(bits) != 8:
        print('Você não adicionou uma sequncia de bits valida')
        continue

    if bits.count('1') % 2 == 0:
        print(f'Para a sequencia de bits {bits} o bit de paridade deve ser 0')
    else:
        print(f'Para a sequencia de bits {bits} o bit de paridade deve ser 1')
