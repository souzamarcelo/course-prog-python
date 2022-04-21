distancia = float(input('Distância (km): '))
velocidade = float(input('Velocidade (km/h): '))
tempo = distancia / velocidade
print('Tempo de viagem estimado é', tempo, ' horas.')

horas = distancia // velocidade
minutos = (tempo - horas) * 60
print('Tempo de viagem estimado é de', horas, ' horas e', minutos, ' minutos.')