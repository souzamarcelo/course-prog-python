n = int(input('Informe o tamanho das listas: '))
a = []
b = []
c = []

for i in range(n):
    a.append(int(input('Informe o elemento %d da lista A: ' % i)))
    b.append(int(input('Informe o elemento %d da lista B: ' % i)))

for i in range(n):
    if i % 2 == 0:
        c.append(a[i])
    else:
        c.append(b[i])

print('Lista A: ' + str(a))
print('Lista B: ' + str(b))
print('Lista C: ' + str(c))