#Exercício ler as palavras e as vogais de cada palavra.
palavras = ('Mario', 'Luigi', 'Peach', 'yoshi', 'bowser')

for palavra in palavras:
    print('\nPalavras: {}. Vogais:'.format(palavra.upper()), end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')  #end='' - serve para não dar quebra de linha no print.