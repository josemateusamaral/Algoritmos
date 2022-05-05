fraseOriginal = input('Digite uma fraze para verificar se esta fraze é um palíndromo: ').lower()
fraseParaTeste = ''
for letra in fraseOriginal:
    if letra not in ' .,!?=-_+()*&¨%$#@!/\\:;><{[]}|': fraseParaTeste += letra

ok = True
for index,letra in enumerate(fraseParaTeste):
    if fraseParaTeste[ (index + 1) * -1 ] != letra:
        ok = False
        break

if ok: print(f'A frase {fraseOriginal} é um palíndromo')
else: print(f'A frase {fraseOriginal} não é um palíndromo')
