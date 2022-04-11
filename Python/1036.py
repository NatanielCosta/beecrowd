import math

a, b, c = list(map(float, input().split(' ')))

delta = pow(b, 2) - 4 * a * c

if delta < 0 or a == 0:
  print('Impossivel calcular')
else:
  r1 = (-b + math.sqrt(delta)) / (2 * a)
  r2 = (-b - math.sqrt(delta)) / (2 * a)
  print('R1 = %.5f\nR2 = %.5f' % (r1, r2))