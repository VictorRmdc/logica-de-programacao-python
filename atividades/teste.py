#c = 0
#while c < 9:
    #print(c)
    #c += 2

#for c in range (0, 9, 2):
    #print(c)
#c += 1



while True:
    valor = input('Digite o valor que deseja retirar: ')
    if valor == 'sair':
        break
    valor = int(valor)
    if valor >= 100:
        cedulas100 = valor // 100
        valor = valor - cedulas100 * 100
        print('quantidade de cedulas de 100 : {}'.format(cedulas100))

    if valor >= 50:
        cedulas50 = valor // 50
        valor = valor - cedulas50 * 50
        print('quantidade de cedulas de 50 :{}'.format(cedulas50))

    if valor >= 20:
        cedulas20 = valor // 20
        valor = valor - cedulas20 * 20
        print('quantidade de cedulas de 20 :{}'.format(cedulas20))

    if valor >= 10:
        cedulas10 = valor // 10
        valor = valor - cedulas10 * 10
        print('quantidade de cedulas de 10 :{}'.format(cedulas10))

    if valor >= 5:
        cedulas5 = valor // 5
        valor = valor - cedulas5 * 5
        print('quantidade de cedulas de 5 :{}'.format(cedulas5))

    if valor >= 1:
        cedulas1 = valor // 1
        valor = valor - cedulas1 * 1
        print('quantidade de cedulas de 1 :{}'.format(cedulas1))
        continue