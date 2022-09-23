preço = float(input('Preço atual do produto: R$'))
desconto = preço - (preço * 20 / 100)
print('O valor que custava R${:.2f} teve um desconto de de 20%, seu produto agora é R${:.2f}'.format(preço, desconto))