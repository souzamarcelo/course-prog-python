modelo = []
consumo = []

for i in range(5):
    modelo.append(input('Informe o modelo do %do veículo: ' % (i + 1)))
    consumo.append(int(input('Informe o consumo do %do veículo: ' % (i + 1))))

indice_economico = 0
maior_economia = float('-inf')
for i in range(len(consumo)):
    if consumo[i] > maior_economia:
        maior_economia = consumo[i]
        indice_economico = i
print('O veículo mais econômico é o %s, que faz %d quilômetros com um litro de combustível!' % (modelo[indice_economico], maior_economia))

for i in range(len(consumo)):
    litros = 1000 / consumo[i]
    print('O veículo %s consome %.1f litros de combustível para percorrer 1000km!' % (modelo[i], litros))