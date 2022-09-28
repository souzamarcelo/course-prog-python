import sys

def tempo(massa):
    t = 0
    while massa >= 0.5:
        t += 50
        massa /= 2
    return t

def massa_final(massa):
    while massa >= 0.5:
        massa /= 2
    return massa


massa_i = float(sys.argv[1])
tempo_f = tempo(massa_i)
massa_f = massa_final(massa_i)

print(tempo_f)
horas = int(tempo_f / 60 / 60)
tempo_f = tempo_f - (horas * 60 * 60)
minutos = int(tempo_f / 60)
tempo_f = tempo_f - (minutos * 60)
segundos = tempo_f

print('Massa inicial: %.1f' % massa_i)
print('Massa final: %.1f' % massa_f)
print('Tempo: %d horas, %d minutos, %d segundos' % (horas, minutos, segundos))