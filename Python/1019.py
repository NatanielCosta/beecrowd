N = int(input())

horas = int(N/3600)
N = N % 3600
minutos = int(N/60)
N = N % 60
segundos = int(N)

print('%d:%d:%d' % (horas, minutos, segundos))