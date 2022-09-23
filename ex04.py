#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2mQuadrado.

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {} metros quadrados.'.format(larg, alt, área))
tinta = área / 2 
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))

real = float(input('Quanto você tem de dinheiro: R$'))
dollar = real / 5.17
print('Você só pode comprar RS${:.2f}'.format(dollar))

#Tentando recriar...
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
m = larg * alt 
print('A largura e altura da sua parede tem {}x{}, ela mede {}m'.format(larg, alt, m))
tinta = m / 2
print('A quantidade de tinta que você precisa para pintar é: {}l'.format(tinta))