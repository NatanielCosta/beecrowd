import math

linha = input().split(' ')

A, B, C = map(float, linha)

triangulo = (A * C) / 2
circulo = 3.14159 * math.pow(C, 2)
trapezio = ((A + B) * C) / 2
quadrado = math.pow(B, 2)
retangulo = A * B

print('TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f' % (triangulo, circulo, trapezio, quadrado, retangulo))