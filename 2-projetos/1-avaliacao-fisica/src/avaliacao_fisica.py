nome = input('Nome do atleta: ')
idade = int(input('Idade: '))
peso = float(input('Peso: '))
altura = float(input('Altura: '))
tempo_100 = int(input('Tempo na corrida de 100m: '))
tempo_1000 = int(input('Tempo na corrida de 1km: '))
batimentos_repouso = int(input('Batimentos cardíacos em repouso: '))
batimentos_leve = int(input('Batimentos cardíacos em atividade leve: '))
batimentos_intensa = int(input('Batimentos cardíacos em atividade intensa: '))
cintura = int(input('Medida da cintura: '))
quadril = int(input('Medida do quadril: '))
doenca_respiratoria = bool(int(input('Possui doença respiratória (0 - NÃO; 1 - SIM): ')))
doenca_cardiaca = bool(int(input('Possui doença cardíaca (0 - NÃO; 1 - SIM): ')))

print('Nome do atleta:', nome, '\n')
print('RELATÓRIO DE MEDIDAS/DADOS')
print('Idade:', idade, 'anos')
print('Peso:', peso, 'kg')
print('Altura:', altura, 'm')
print('Tempo na corrida de 100m:', tempo_100, 's')
print('Tempo na corrida de 1km:', tempo_1000, 's')
print('Batimentos cardíacos em repouso:', batimentos_repouso)
print('Batimentos cardíacos em atividade leve:', batimentos_leve)
print('Batimentos cardíacos em atividade intensa:', batimentos_intensa)
print('Medida da cintura:', cintura, 'cm')
print('Medida do quadril:', quadril, 'cm')
print('Possui doença respiratória?', doenca_respiratoria)
print('Possui doença cardíaca?', doenca_cardiaca)

imc = peso / (altura ** 2)
tempo_100_h = tempo_100 / 60 / 60
v_c = 0.1 / tempo_100_h
tempo_1000_h = tempo_1000 / 60 / 60
v_m = 1 / tempo_1000_h
b_r = batimentos_repouso / 10
b_l = batimentos_leve / 10
b_i = batimentos_intensa / 10
rcq = cintura / quadril

imc_min = 19
imc_max = 22
v_c_min = 9
v_m_min = 7
b_r_min = 65
b_r_max = 80
b_l_min = 80
b_l_max = 120
b_i_min = 90
b_i_max = 150
rcq_min = 0.8
rcq_max = 0.9

imc_adequado = (imc_min <= imc <= imc_max)
v_c_adequado = (v_c >= v_c_min)
v_m_adequado = (v_c >= v_m_min)
b_r_adequado = (b_r_min <= b_r <= b_r_max)
b_l_adequado = (b_l_min <= b_l <= b_l_max)
b_i_adequado = (b_i_min <= b_i <= b_i_max)
rcq_adequado = (rcq_min <= rcq <= rcq_max)

print('\n\nRELATÓRIO DE INDICADORES (ADEQUADO?)')
print('IMC: %3.1f --> ' % imc + str(imc_adequado))
print('Vc: %3.1f --> ' % v_c + str(v_c_adequado))
print('Vm: %3.1f --> ' % v_m + str(v_m_adequado))
print('Br: %4.1f --> ' % b_r + str(b_r_adequado))
print('Bl: %4.1f --> ' % b_l + str(b_l_adequado))
print('Bi: %4.1f --> ' % b_i + str(b_i_adequado))
print('RCQ: %3.2f --> ' % rcq + str(rcq_adequado))


peso_desejado_min = 19 * altura ** 2
peso_desejado_max = 22 * altura ** 2
tempo_100_desejado = 360 / 9
tempo_1000_desejado = 3600 / 7
b_r_desejado_min = 65 * 10
b_r_desejado_max = 80 * 10
b_l_desejado_min = 80 * 10
b_l_desejado_max = 120 * 10
b_i_desejado_min = 90 * 10
b_i_desejado_max = 150 * 10

print('\n\nRELATÓRIO DE SUGESTÕES')
print('Seu peso deve ficar entre %.1f e %.1f.' % (peso_desejado_min, peso_desejado_max))
print('Seu tempo no tiro curto (100m) deve ser no mínimo %.1f.' % (tempo_100_desejado))
print('Seu tempo no tiro médio (1000m) deve ser no mínimo %.1f.' % (tempo_1000_desejado))
print('Seus batimentos caríacos em repouso (10min) devem estar entre %d e %d.' % (b_r_desejado_min, b_r_desejado_max))
print('Seus batimentos caríacos em atividade leve (10min) devem estar entre %d e %d.' % (b_l_desejado_min, b_l_desejado_max))
print('Seus batimentos caríacos em atividade intensa (10min) devem estar entre %d e %d.' % (b_i_desejado_min, b_i_desejado_max))

alerta1 = imc > imc_max and doenca_cardiaca
alerta2 = imc > imc_max and (b_l > b_l_max or b_i > b_i_max)
alerta3 = (v_c < v_c_min or v_m < v_m_min) and (b_l > b_l_max or b_i > b_i_max)
alerta4 = (rcq < rcq_min or rcq > rcq_max) and doenca_respiratoria
alerta5 = doenca_respiratoria and doenca_cardiaca
alerta6 = idade > 40 and (rcq < rcq_min or rcq > rcq_max)
alerta7 = idade >= 18 and idade <= 60 and b_r < b_r_min
alerta8 = (rcq < rcq_min or rcq > rcq_max) and imc > imc_max and (v_c < v_c_min or v_m < v_m_min)

print('\n\nRELATÓRIO DE ALERTAS')
print('(True para alerta ativado; False quando não se aplica)')
print('1. IMC acima + problemas cardíacos: ' + str(alerta1))
print('2. IMC acima + batimentos altos (atividade leve ou intensa): ' + str(alerta2))
print('3. Velocidade (tiro curto ou médio) abaixo + batimentos altos (atividade leve ou intensa): ' + str(alerta3))
print('4. RCQ inadequado + problemas respiratórios: ' + str(alerta4))
print('5. Problemas respiratórios e cardíacos: ' + str(alerta5))
print('6. Maior de 40 anos + RCQ inadequado: ' + str(alerta6))
print('7. Entre 18 e 60 anos + batimentos baixos em repouso: ' + str(alerta7))
print('8. RCQ inadequado + IMC acima + velocidade (tiro curto ou médio) abaixo: ' + str(alerta8))