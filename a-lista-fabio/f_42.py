x1 = int(input('Digite o valor de x no ponto1: '))
y1 = int(input('Digite o valor de y no ponto1: '))
x2 = int(input('Digite o valor de x no ponto2: '))
y2 = int(input('Digite o valor de y no ponto2: '))

import math

print(f'O resultado da expressão equivale a {math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2): .2f}')