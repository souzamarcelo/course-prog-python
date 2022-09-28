numeros = [0] * 10
for i in range(10):
    numeros[i] = int(input('Informe o valor da posição %d: ' % i))

x = int(input('Informe o valor de x: '))
y = int(input('Informe o valor de y: '))

print(numeros[x] + numeros[y])