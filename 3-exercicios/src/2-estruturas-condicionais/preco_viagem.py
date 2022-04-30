km = float(input('Distância a percorrer: '))

if km <= 200:
    preco = km * 0.5
else:
    preco = km * 0.45

print('Preço da passagem: %.1f' % preco)