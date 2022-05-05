print(end='\t')
for i in range(1,11):
    print(i,end='\t')
print()

for numero in range(1,11):
    print(numero,end='\t')
    for n in range(10):
        print(numero + (n * numero),end='\t')
    print()
