import sys

salario_minimo = float(sys.argv[1])
quilowatts = float(sys.argv[2])

valor_quilowatt = salario_minimo / 5
conta = valor_quilowatt * quilowatts
conta_desconto = conta - conta * 0.15

print('Valor do quilowatt: %.2f' % valor_quilowatt)
print('Valor da conta: %.2f' % conta)
print('Valor da conta com desconto: %.2f' % conta_desconto)