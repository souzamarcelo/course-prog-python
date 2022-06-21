valores = []

for _ in range(10):
    valores.append(int(input('Informe um valor: ')))

x = int(input('Informe o valor a ser buscado: '))

for i in range(len(valores)):
    if valores[i] == x:
        print('Valor encontrado na posição %d!' % i)
        exit()
print('Valor %d não encontrado na lista %s' % (x, valores))