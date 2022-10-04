def tipo_triangulo(x, y, z):
    if x >= y + z or y >= x + z or z >= x + y:
        return 'NÃO É UM TRIÂNGULO'
    elif x == y and y == z:
        return 'TRIÂNGULO EQUILÁTERO'
    elif x == y or y == z or x == z:
        return 'TRIÂNGULO ISÓSCELES'
    else:
        return 'TRIÂNGULO ESCALENO'

import sys

for i in range(3, 16, 3):
    x = int(sys.argv[i - 2])
    y = int(sys.argv[i - 1])
    z = int(sys.argv[i])
    print(x, y, z, '---', tipo_triangulo(x, y, z))