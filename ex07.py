# Escreva um programa que converta uma temperatuar digitada em °C e coverta em °F.

c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5 ) + 32
print('A temperatura de {0}°c corresponde a {1}°F!'.format(c, f))

#Temperatuar digitada em °f e coverta em °C

f = float(input('Informe a temperatura em °F: '))
c = ((f - 32) / 1.8)
print('A temperatura de {}°F corresponde a {}°C!'.format(f, c))