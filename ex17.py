#Crie um programa que leia onome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('seu nome tem Silva?. {}'.format('SILVA' in nome.upper()))