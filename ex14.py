#Crie um programa que leia o nome completo de um e mostre: 
#-O nomem com todas as letras maiúsculas e minúsculas.
#-Quantas letras ao todo(sem considerar espaços).
#-Quantas letras tem o primeiro nome.

'''nome = str(input('Digite seu nome completo: ')).strip() #Remove espaços inúteis 
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' '))) #Conta quantas letras tem e espaços (count)
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))'''

#Praticando...
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))

nome = str(input('Digite seu nome completo: ')).strip()
print('O seu nome em maiúsculas é {}'.format(nome.upper()))
print('O seu nome em minúsculas é {}').format(nome.lower())
print('o seu nome completo possui {} letras'.format(len(nome)-nome.count(' ')))

separa = nome.split()
print('o seu completo é {} e o seu primiero nome é {}'.format(separa[0], len(separa[0])))
