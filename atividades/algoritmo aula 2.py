# Solicitar O preço e porcemtagem de desconto e realizar o calculo do valor final.

# Float declara o tipo de dado que será quardado na variavel.
preco = float(input('Qual é o preço do produto :'))
p = float(input('Qual é o percentual de desconto (0-100) % :'))

Des = preco * (p / 100)
final = preco - Des

print('O preço do produto é {}. Desconto de {}%.'.format(preco, p))
print('Valor calculado de desconto: {}. valor final do produto: {}'. format(Des, final))