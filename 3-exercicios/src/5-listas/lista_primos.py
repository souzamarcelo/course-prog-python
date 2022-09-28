import sys

argumentos = sys.argv[1:]
lista = []
for item in argumentos:
    lista.append(int(item))

print(lista)

primos = []
for numero in lista:
    primo = True
    if numero <= 1: primo = False
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo: primos.append(numero)

print(primos)