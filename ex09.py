#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
'''
import math
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

from math import trunc 
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção interira é {}'.format(num, trunc(num)))

num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
'''

import math
num = float(input('Digite um número: '))
print('O seu valor real é {} e o seu valor inteiro é {}'.format(num, math.trunc(num)))

from math import trunc
num = float(input('Digite um número: '))
print('O seu valor real é {} eo seu valor inteiro {}'.format(num, trunc(num)))

num1 = float(input('Digite um número: '))
num2 = int(num1)
print('O seu valor real é {} e o seu valor inteiro {}'.format(num1, num2))