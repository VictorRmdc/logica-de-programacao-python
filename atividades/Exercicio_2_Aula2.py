# Exercicio 02 de lógica. Valor de cada dia de locação 60R$ e 0.15 por km rodado.
Km= int(input('Quantidade de Km percorridos :'))
D = int(input('Quantidade de dias de locação: '))

Vkm = Km * 0.15
dias = D * 60.00
total = Vkm + dias

print('O valor a ser cobrado por {} Km rodados é {} .'.format(Km, Vkm))
print('O valor a ser cobrado pelos {} dias de locação é {}'.format(D, dias))
print('O valor total da locação é {}'.format(total))

# segunda forma de execução.

Km1= int(input('Quantidade de Km percorridos :'))
D1 = int(input('Quantidade de dias de locação: '))

preco = 60 * D1 + 0.15 * Km1
print('Km = {}. Dias {}'.format(Km1, D1))
print('Valor total a ser pago: {}'.format(preco))

