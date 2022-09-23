#Faça um programa que leia o comprimento do cateto oposto e do catetto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente'))
hi = (co ** 2 + ca ** 2 ) ** (1/2)
print('A hipotenusa vai medir {}'.format(hi))

#Com importação

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

from math import hypot
co = float(input('Comprimento do cateto oposto: ')) 
ca = float(input('Comprimento do cateto adjancente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))