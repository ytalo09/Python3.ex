#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex: Digite um número: 1834
#>>> unidade: 4 dezena:3 centena:8 milhar:1


num = int(input('Digite um número: '))
n = str(num)
print('Analizando o número {}'.format(num))
print('Unidade {}'.format(n[3]))
print('Dezena {}'.format(n[2]))
print('Centena {}'.format(n[1]))
print('Milhar {}'.format(n[0]))

#Da forma matemáticamente...
num = int(input('Informe o número: '))
a = num // 1 % 10
b = num // 10 % 10
c = num // 100 % 10 
d = num // 1000 % 10
print('Analizando número {}'.format(num))
print('Unidade: {}'.format(a))
print('Dezena: {}'.format(b))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(d))