idade = int(input())

anos = int(idade / 365)
idade = idade % 365

meses = int(idade / 30)
idade = idade % 30

dias = idade

print('%d ano (s)\n%d mes (es)\n%d dia (s)' % (anos, meses, dias))
'1 ano(s)\n1 mes(es)\n5 dia(s)'