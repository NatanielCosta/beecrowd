valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
  qtdCedulas = int(valor/nota)
  print('%d nota(s) de R$ %d.00' % (qtdCedulas, nota))
  valor = valor % nota

print('MOEDAS:')
for moeda in moedas:
  qtdMoedas = int(valor/moeda)
  print('%d moeda(s) de R$ %.2f' % (qtdMoedas, moeda))
  valor = round(valor % moeda, 2)