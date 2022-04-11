linha = input().split(' ')

a, b, c = map(int, linha)

maiorAB = (a + b + abs(a-b)) / 2
maiorXC = (maiorAB + c + abs(maiorAB - c)) / 2

print('%d eh o maior' % maiorXC)