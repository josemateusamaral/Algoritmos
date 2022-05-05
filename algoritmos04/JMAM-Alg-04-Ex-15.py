result = ''
q = int(input('Digite um número decimal para convertelo para binário: '))
while q != 0:
    r = q % 2
    r = str(r)
    result = r + result
    q = q // 2
print(result)
