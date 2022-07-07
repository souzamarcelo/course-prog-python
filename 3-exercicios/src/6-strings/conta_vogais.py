def conta_vogais_caractere(texto):
    qtd_a = 0
    qtd_e = 0
    qtd_i = 0
    qtd_o = 0
    qtd_u = 0
    texto = texto.lower()
    for caractere in texto:
        if caractere == 'a':
            qtd_a += 1
        if caractere == 'e' or caractere == 'é':
            qtd_e += 1
        if caractere == 'i':
            qtd_i += 1
        if caractere == 'o':
            qtd_o += 1
        if caractere == 'u':
            qtd_u += 1

    total = qtd_a + qtd_e + qtd_i + qtd_o + qtd_u
    print('Quantidade a: %d' % qtd_a)
    print('Quantidade e: %d' % qtd_e)
    print('Quantidade i: %d' % qtd_i)
    print('Quantidade o: %d' % qtd_o)
    print('Quantidade u: %d' % qtd_u)
    print('Quantidade total de vogais: %d' % total)

def conta_vogais_count(texto):
    texto = texto.lower()
    qtd_a = texto.count('a')
    qtd_e = texto.count('e')
    qtd_i = texto.count('i')
    qtd_o = texto.count('o')
    qtd_u = texto.count('u')
    total = qtd_a + qtd_e + qtd_i + qtd_o + qtd_u
    print('Quantidade a: %d' % qtd_a)
    print('Quantidade e: %d' % qtd_e)
    print('Quantidade i: %d' % qtd_i)
    print('Quantidade o: %d' % qtd_o)
    print('Quantidade u: %d' % qtd_u)
    print('Quantidade total de vogais: %d' % total)
    return total

frase = input('Digite uma frase: ')
print(frase)
#conta_vogais_caractere(frase)
vogais = conta_vogais_count(frase)
nao_vogais = len(frase) - vogais
print('Quantidade total de não vogais: %d' % nao_vogais)