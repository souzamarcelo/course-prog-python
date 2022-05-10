import sys

deposito = float(sys.argv[1])
taxa = float(sys.argv[2])

montante = deposito
for i in range(1, 25):
    montante = montante + (montante * taxa)
    print('Mês %d: R$ %.2f' % (i, montante))