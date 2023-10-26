#Exercicio4
print('Escolha o que você deseja comprar: ')
print('1-Maçâ')
print('2-Laranja')
print('3-Banana')

P = int(input('Qual é sua escolha ?'))
Q = int(input('Quantas unidades ?'))

if P == 1 :
    pagar = Q * 2.3
    print('Você comprou {} maças. Total a pagar {}'.format(Q, pagar))
else:
    if P == 2 :
        pagar = Q * 3.6
        print('Você comprou {} Laranja. Total a pagar {}'.format(Q, pagar))
    else:
        if P == 3 :
            pagar = Q * 1.85
            print('Você comprou {} Banana. Total a pagar {}'.format(Q, pagar))
        else:
            print('Produto inexistente')


#Exercicio4 forma 2 de executar com elif
print('Escolha o que você deseja comprar: ')
print('1-Maçâ')
print('2-Laranja')
print('3-Banana')

P = int(input('Qual é sua escolha ?'))
Q = int(input('Quantas unidades ?'))

if P == 1 :
    pagar = Q * 2.3
    print('Você comprou {} maças. Total a pagar {}'.format(Q, pagar))
elif (P == 2) :
    pagar = Q * 3.6
    print('Você comprou {} Laranja. Total a pagar {}'.format(Q, pagar))
elif P == 3 :
    pagar = Q * 1.85
    print('Você comprou {} Banana. Total a pagar {}'.format(Q, pagar))
else:
    print('Produto inexistente')



