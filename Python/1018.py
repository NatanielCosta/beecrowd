valor = int(input())
print(valor)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
  qtdCedulas = int(valor/nota)
  print('%d nota(s) de R$ %d,00' % (qtdCedulas, nota))
  valor = valor % nota