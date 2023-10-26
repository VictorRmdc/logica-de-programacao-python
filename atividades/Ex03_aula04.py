total = 0 # essa variavel receberá o total de idade
dinheiro = 0 # Essa variável recebrá o total arrecadado.

while True:
    idade= input('Qual é sua idade? ')
    if idade == 'sair':
        break
    idade = int(idade) #linha criada, pois se o cliente não digitar sair que é string, a variavel se tornará inteira.
    total += 1
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso
media = dinheiro/total

print('Total de pessoas {}'.format(total))
print('Total arrecadado {}'.format(dinheiro))
print('Média {}'.format(media))
