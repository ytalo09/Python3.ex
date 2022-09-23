#Crie um programa que leia quanto dinheiro uma pesssoa tem na carteira e mostre quantos Dólares ela pode comprar.

#Considere US$1,00 = R$3,27 --> dollar divide, real multiplica-

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))

#Calculadora

número = int(input('Digite o número que você qué ver a tabuada: '))
print('-' *12)
print('{} x {} = {}'.format(número, 1, número*1))

real = int(input('Quanto de dinherio você tem na carteira: R$'))
dollar = real / 5.17
print('Você pode só comprar: R${:.2f}'.format(dollar))