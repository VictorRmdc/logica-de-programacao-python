print('Bem vindo a loja do Victor Hugo Miranda Carneiro')

valor_produto = float(input('Entre com o valor do produto: ')) # Solicitado a entrada do valor do produto.
qtd_produto = int(input('Entre com a quantidade do produto')) # Solicitado a entrada da quantidade de produto.

desconto = 0 # desconto começa o programa = 0

if qtd_produto < 200:
    desconto = 0.00 # 100 = 1.0 /  abaixo de qtd 200, não possui desconto.
elif (qtd_produto >= 200) and (qtd_produto< 1000):
    desconto =  0.05 # 100 = 1.0 / 0.05 = 5%
elif (qtd_produto >= 1000) and (qtd_produto < 2000):
    desconto = 0.10 # 100 = 1.0 / 0.10 = 10%
else:
    desconto = 0.15 # se a quantidade for acima de 2000, o desconto será de 15%. 100% = 1.0/ 0.15 = 15 %

total_sem_desconto =  valor_produto * qtd_produto
print("O valor total do produto sem desconto é R$ {:.2f}".format(total_sem_desconto))
total_de_desconto = total_sem_desconto * desconto # Também é possível obter o resultado dessa forma (total_de_desconto = total_sem_desconto  - total_sem_desconto * desconto)
valor_final_desconto = total_sem_desconto - total_de_desconto # definindo o valor.
print("O valor total do produto com desconto é {:.2f}".format(valor_final_desconto)) # Valor final com o desconto aplicado.