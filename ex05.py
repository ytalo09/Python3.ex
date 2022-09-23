#Façaum algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Qual é o preço do produto? R$'))
desconto = produto - (produto * 5 / 100)
print('O produto que custava R${}, na promoção com descoto de 5% vai custar {}'.format(produto, desconto))

#tentando recriar...
preço = float(input('Qual o preço do produto: '))
desconto = preço - (preço * 5 / 100) #porcentagem --> preço do produto multiplicado por 5 dividido po 100
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${}'.format(preço, desconto))