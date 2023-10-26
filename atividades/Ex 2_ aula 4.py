# Exercício 2, Escreva um algoritmo que leia um valor e imprima a quantidade de cédulas desse valor.
#trabalharemos somente com valores inteiros.
valor = int(input('Digite um valor em R$: '))

while True:
    if valor >= 100:
        cedula100 = valor // 100
        valor = valor - cedula100 * 100 # (ou valor - = cedula100 *), Lógica, ex: valor recebeu 522 - celula de 100 que é 5 x 100. ficou (522 - 5 * 100). Basicamente 522 - 500
        print('Cédulas de 100 : {}'.format(cedula100))
        if not valor: # Caso o valor fique com o valor zero será realizado o break e operação é encerrada, pois a informação passará a ser false.
            break
    if valor >= 50:
        cedula50 = valor // 50
        valor = valor - cedula50 * 50
        print('Cédulas de 50 : {}'.format(cedula50))
        if not valor:
            break
    if valor >= 20:
        cedula20 = valor // 20
        valor = valor - cedula20 * 20
        print('Cédulas de 20 : {}'.format(cedula20))
        if not valor:
            break
    if valor >= 10:
        cedula10 = valor // 10
        valor = valor - cedula10 * 100
        print('Cédulas de 10 : {}'.format(cedula10))
        if not valor:
            break
    if valor >= 5:
        cedula5 = valor // 5
        valor = valor - cedula5 * 5
        print('Cédulas de 5 : {}'.format(cedula5))
        if not valor:
            break
    if valor:
        cedula1 = valor
        print('Cédulas de 1 : {}'.format(cedula1))
        break