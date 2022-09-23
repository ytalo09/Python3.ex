#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

'''
import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))

print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))

print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))
'''

# Praticando...

import math
ângulo = float(input('Digite um ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print('o ângulo {} é o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo {} é o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo {} é a TANGENTE de {:.2f}'.format(ângulo, tangente))

'''
import math
num = float(input('Digite um número: '))
print('O valor real é {} e o valor inteiro {}'.format(num, math.trunc(num)))
'''
num1 = float(input('Digite um número: '))
print('O seu valor real é {} e o seu valor inteiro {}'.format(num1, int(num1)))

