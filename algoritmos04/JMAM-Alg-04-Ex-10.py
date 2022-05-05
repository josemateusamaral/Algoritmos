palavra = input('Digite uma palavra para verificar se esta palavra é um palíndromo: ').lower()
ok = True
for index,letra in enumerate(palavra):
    if palavra[ (index + 1) * -1 ] != letra:
        ok = False
if ok: print(f'A palavra {palavra} é um palíndromo')
else: print(f'A palavra {palavra} não é um palíndromo')
