casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Quanto você recebe de salário? R$'))
anos = int(input('Quantos anos você deseja pagar essa casa? '))
prestação = casa / (anos * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')