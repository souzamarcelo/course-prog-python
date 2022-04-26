import sys

numero = float(sys.argv[1])

parte_inteira = int(numero)
parte_fracionaria = numero - parte_inteira

print('Parte inteira: %d' % parte_inteira)
print('Parte fracionária: %f' % parte_fracionaria)
print('Arredondamento para uma casa decimal: %.1f' % numero)
print('Arredondamento para um inteiro: %d' % round(numero))