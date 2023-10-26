kwh= float(input('Quantos Kwh?'))
Tipo=input('Qual é o tipo de instalação (R, C ou I)')

if Tipo == 'R':
    if kwh <= 500:
        preco = 0.4
    else:
        preco =0.65
elif Tipo == 'C':
    if kwh <= 1000:
        preco = 0.55
    else:
        preco =0.60
elif Tipo == 'I':
    if kwh <= 5000:
        preco = 0.55
    else:
        preco =0.6
else:
    print('Instalação inválida')

print('Total a pagar : {}'.format(kwh * preco))