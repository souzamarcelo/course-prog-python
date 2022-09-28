def divisores(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
    return div

def perfeito(n):
    soma = 0
    for d in divisores(n):
        soma += d
    return n == soma


import sys
n = int(sys.argv[1])
print('n = %d' % n)
print('Divisores: ' + str(divisores(n)))
if perfeito(n): print('%d é um número perfeito!' % n)
else: print('%d NÃO é um número perfeito!' % n)