velocidade = input('Velocidade: ')
velocidade = int(velocidade)

if velocidade > 80:
    print('Você foi multado!')
    valor_multa = (velocidade - 80) * 30
    print('A multa é de $%.2f.' % valor_multa)