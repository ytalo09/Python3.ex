nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal')
print('Bom dia {}!'.format(nome))

n1 = int(input('Digite a primiera nota: '))
n2 = int(input('Digite outra nota:'))
média = (n1 + n2) / 2
if média >= 6.0:
    print('PARABÉNS! sua média foi boa!')
else:
    print('Precisa melhorar Boy!')
print('Sua nota foi {:.1f}'.format(média))
