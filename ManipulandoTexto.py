frase = 'curso em Video Python'
print(frase[::2])

frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))

frase = '    Curso em Vídeo Python' # Conta os espaços também
print(len(frase))

frase = '      Curso em Vídeo Python' # Não conta com os espaços
print(len(frase.strip()))

frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))

frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Android')
print(frase)

frase = 'Curso em vídeo Python'
print('Curso' in frase)

frase = 'Curso em Vídeo Python'
print(frase.find('Vídeo'))

frase = 'curso em Vídeo Python'
print(frase.lower().find('Vídeo'))

frase = 'Curso em Vídeo Python'
print(frase.split())

frase = 'curso em vídeo Python'
dividido = frase.split()
print(dividido[0])

frases = 'curso em Vídeo Python'
dividido = frase.split()
print(dividido[2] [3])
print("""As linguagens formais são linguagens criadas pelas pessoas para aplicações específicas.
Por exemplo, a notação que os matemáticos usam é uma linguagem formal especialmente
boa para denotar relações entre números e símbolos. Os químicos usam uma linguagem
formal para representar a estrutura química de moléculas. E o mais importante:""")