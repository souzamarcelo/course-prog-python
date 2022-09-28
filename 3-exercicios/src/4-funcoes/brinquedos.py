import math

def leitura():
    a = int(input('Informe o valor da primeira dimensão: '))
    if a == -1:
        return None
    b = int(input('Informe o valor da segunda dimensão: '))
    c = int(input('Informe o valor da terceira dimensão: '))
    return [a, b, c]

def calcula_d(a, b, c):
    return math.sqrt((a ** 2) + (b ** 2) + (c ** 2))

esferas_10 = 0
esferas_15 = 0
esferas_20 = 0
esferas_25 = 0
maior_25 = 0

dados = leitura()
while dados != None:
    a = dados[0]
    b = dados[1]
    c = dados[2]
    d = calcula_d(a, b, c)
    if d > 25:
        maior_25 += 1
    elif d > 20:
        esferas_25 += 1
    elif d > 15:
        esferas_20 += 1
    elif d > 10:
        esferas_15 += 1
    else:
        esferas_10 += 1

    dados = leitura()

print(f'Esferas 10cm: {esferas_10}')
print(f'Esferas 15cm: {esferas_15}')
print(f'Esferas 20cm: {esferas_20}')
print(f'Esferas 25cm: {esferas_25}')
print(f'Caixas com diagonal maior que 25cm: {maior_25}')
