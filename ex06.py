#Reajuste Salarial.

#Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input('Qual o salário do Funcionário? R$'))
aumento = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R$ R${:.2f}'.format(salário, aumento))