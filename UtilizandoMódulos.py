
import math #Biblioteca padrão (math). Significado: Matemática
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

#Praticando...

import math 
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é {}'.format(num, raiz))

#Estudo

from math import sqrt #Selecionando o tipo de módulo que quero. Usando 'from'
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadra de {} é igual á {}'.format(num, raiz))

from math import sqrt, floor #Utilizando mais de um módulo
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é {}'.format(num, floor(raiz)))

#Jeito tradicional.

num = int(input('Digite um número: '))
raiz = num ** (1/2)
print('A raiz quadrada de {} é {}'.format(num, raiz))
 
num = int(input('Digite um número: '))
print('A raiz quadrada de {} é {}'.format(num**(1/2)))

import random #Gerar números aleatórios 
num = random.random()
print(num)


