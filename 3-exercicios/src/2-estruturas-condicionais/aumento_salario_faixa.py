salario = float(input('Informe salário: '))

if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

print('Aumento: %.1f' % aumento)