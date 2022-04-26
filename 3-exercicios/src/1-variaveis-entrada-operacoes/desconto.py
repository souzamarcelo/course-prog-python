import sys

preco = float(sys.argv[1])
percentual = float(sys.argv[2])
valor_desconto = preco * percentual / 100
valor_pagar = preco - valor_desconto

print('O valor de desconto é $%.2f, e o preço a pagar é $%.2f.' % (valor_desconto, valor_pagar))