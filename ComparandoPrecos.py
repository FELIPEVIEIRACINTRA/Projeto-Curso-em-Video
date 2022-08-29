Total = TotP = menor = cont = 0
barato = ' '
while True:
    Produto = str(input('Digito o protudo que queira comprar: '))
    Preço = float(input('Qual o valor do produto: '))
    cont += 1
    Total += Preço
    if Preço > 1000:
        TotP += 1
    if cont == 1:
        menor = Preço
        barato = Produto
    else:
        if Preço < menor:
            menor = menor
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi {Total:10.2f}')
print(f'Temos {TotP} produtos custando mais de R$1000.00')
print(f'O produto mais barato {barato} custa R$ {menor:.2f}')