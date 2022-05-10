import sys

numerador = int(sys.argv[1])
denominador = int(sys.argv[2])

divisao_inteira = 0

while numerador >= denominador:
    numerador = numerador - denominador
    divisao_inteira = divisao_inteira + 1

print('Divisão inteira:', divisao_inteira)
print('Resto:', numerador)