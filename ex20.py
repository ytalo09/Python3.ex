#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usúario tentar deescobrir qualfoi o número escolhido pelo comptador. O programa deverá escrever na telase o usário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)# Faz o computador "SORTEAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente divinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')

