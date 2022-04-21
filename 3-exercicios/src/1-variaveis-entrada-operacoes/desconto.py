preco = float(input('Preço da mercadoria: '))
percentual = float(input('Percentual de desconto: '))
valor_desconto = preco * percentual / 100
valor_pagar = preco - valor_desconto

print('O valor de desconto é $%.2f, e o preço a pagar é $%.2f.' % (valor_desconto, valor_pagar))