print('Bem vindo a sorveteria do Victor Hugo Miranda Carneiro')
print('---------------------------------Cardápio-----------------------------------------')
print('|N° DE BOLAS | SABOR TRADICIONAL (tr) | SABOR PREMIUM (pr)  | SABOR ESPECIAL (es) |')
print('|    1       |         R$ 6,00        |         R$ 7,00     |        R$ 8,00      |')
print('|    2       |         R$ 10,00       |         R$ 12,00    |        R$ 14,00     |')
print('|    3       |         R$ 14,00       |         R$ 17,00    |        R$ 20,00     |')
print('----------------------------------------------------------------------------------')

total = 0 # O meu total começa o programa valendo zero.
while True:
    sabor = input('Selecione o sabor desejado (tr / pr / es) ?') # Aqui está sendo validado se o valor digitado e o que temos no cardapio.
    if sabor != 'tr' and sabor != 'pr' and sabor != 'es':
        print('Sabor inválido') # caso não seja o cliente é informado que e sabor é inválido.
        continue
    bola = input('Selecione a quantidade de bolas (1 / 2 / 3)?')

    if bola != '1' and bola != '2' and bola != '3': # Aqui está sendo validado se o valor digitado e o que temos no cardapio.
        print('Números de bolas incorretos')
        continue

    if sabor == 'tr' and bola == '1':
        print('Você pediu uma bola de sorvete no sabor tradicional  no valor de R$ 6,00')
        total = total + 6.00 # Aqui a variável total recebe o seu valor mais o valor do item.

    elif sabor == 'tr' and bola == '2':
        print('Você pediu duas bolas de sorvete no sabor tradicional  no valor de R$ 10,00')
        total = total + 10.00 # Aqui a variável total recebe o seu valor mais o valor do item.

    elif sabor == 'tr' and bola == '3':
        print('Você pediu três bolas de sorvete no sabor tradicional  no valor de R$ 14,00')
        total = total + 14.00 # Aqui a variável total recebe o seu valor mais o valor do item.

    elif sabor == 'pr' and bola == '1':
        print('Você pediu uma bola de sorvete no sabor premium  no valor de R$ 7,00')
        total = total + 7.00 # Aqui a variável total recebe o seu valor mais o valor do item.

    elif sabor == 'pr' and bola == '2':
        print('Você pediu duas bolas de sorvete no sabor premium  no valor de R$ 12,00')
        total = total + 12.00 # Aqui a variável total recebe o seu valor mais o valor do item.

    elif sabor == 'pr' and bola == '3':
        print('Você pediu três bolas de sorvete no sabor premium  no valor de R$ 17,00')
        total = total + 17.00 # Aqui a variável total recebe o seu valor mais o valor do item.

    elif sabor == 'es' and bola == '1':
        print('Você pediu uma bola de sorvete no sabor especial  no valor de R$ 8,00')
        total = total + 8.00 # Aqui a variável total recebe o seu valor mais o valor do item.

    elif sabor == 'es' and bola == '2':
        print('Você pediu duas bolas de sorvete no sabor premium  no valor de R$ 14,00')
        total = total + 14.00 # Aqui a variável total recebe o seu valor mais o valor do item.

    elif sabor == 'es' and bola == '3':
        print('Você pediu três bolas de sorvete no sabor especial  no valor de R$ 20,00')
        total = total + 20.00 # Aqui a variável total recebe o seu valor mais o valor do item.

    pedido = input('Você deseja realizar mais um pedido S/N ?') # Aqui é questionado se o cliente deseja realizar um novo pedido.
    if pedido.upper() == 'S': # Utilizo a função item, pois mesmo o cliente digitando minusculo, a variavel receberá em maiusculo.
        continue # se sim, o laço será repetido
    elif pedido.upper() =='N':
        print('O valor total de seu pedido foi : R${:.2f}'.format(total)) # Aqui é mostrado o valor total do pedido.
        break # se não, o laço será encerrado.

