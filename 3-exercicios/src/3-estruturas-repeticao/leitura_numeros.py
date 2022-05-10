numero = int(input('Informe número: '))
soma = 0
quantidade = 0

while numero != 0:
    quantidade = quantidade + 1
    soma = soma + numero
    numero = int(input('Informe número: '))

print('Quantidade: %d' % quantidade)
print('Soma: %d' % soma)
print('Média: %.1f' % (soma / quantidade))