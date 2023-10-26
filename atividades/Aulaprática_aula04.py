# Laço de repetição com while e for
# laço de repetição urilizando for
#for i in range(3,13,1):
    #print(i)

# laço de repetição urilizando while
#i = 3
#while(i <= 12):
    #print(i)
    #i = i + 1 ou i += 1

#for i in range(0, 9, 2):
    #print(i)

# Ex, inteiros de 0 até 9, excluindo 9, com passo de 2
i = 0
#while (i < 9) :
    #print(i)
    #i += 2 #ou i = i + 2

# Exercício 1

# Calculadora utilizando o elif

print('-----------------')
print('SELECIONE A OPERAÇÃO')
print('[ + ]')
print('[ - ]')
print('[ * ]')
print('[ / ]')
print('--------------------')

print('--------------------')


while True:
    Operacao = (input('Selecione a opção operação:'))
    if Operacao == '+' or Operacao == '-' or Operacao == '*' or Operacao == '/':
        N1 = int(input('Digite o primeiro valor'' '))
        N2 = int(input('Digite o primeiro valor'' '))
    else:
        print('Opção inexistente')

    if Operacao == '+':
        Resultado = N1 + N2
        print('A soma de {} + {} é {}'.format(N1, N2, Resultado))
        continue
    elif Operacao == '-':
        Resultado = N1 - N2
        print('A Subtração de {} - {} é {}'.format(N1, N2, Resultado))
        continue
    elif Operacao == '*':
        Resultado = N1 * N2
        print('A multiplicação de {} x {} é {}'.format(N1, N2, Resultado))
        continue
    elif Operacao == '/':
        Resultado = N1 / N2
        print('A divisão de {} / {} é {}'.format(N1, N2, Resultado))
        continue
    elif Operacao == 's':
        break
    else:
        print('operação inválida')

print('Encerrando o programa')




# Calculadora utilizando o elif

print('-----------------')
print('SELECIONE A OPERAÇÃO')
print('[ + ]')
print('[ - ]')
print('[ * ]')
print('[ / ]')
print('--------------------')
Operacao = (input('Selecione a opção operação:'))
print('--------------------')
if Operacao == '+' or Operacao == '-' or Operacao == '*' or Operacao == '/':
    N1 = int(input('Digite o primeiro valor'' '))
    N2 = int(input('Digite o primeiro valor'' '))
else:
    print('Opção inexistente')

while(Operacao != 's'):

    if Operacao == '+':
        Resultado = N1 + N2
        print('A soma de {} + {} é {}'.format(N1, N2, Resultado))
    elif Operacao == '-':
        Resultado = N1 - N2
        print('A Subtração de {} - {} é {}'.format(N1, N2, Resultado))
    elif Operacao == '*':
        Resultado = N1 * N2
        print('A multiplicação de {} x {} é {}'.format(N1, N2, Resultado))
    elif Operacao == '/':
        Resultado = N1 / N2
        print('A divisão de {} / {} é {}'.format(N1, N2, Resultado))
    else:
        print('operação inválida')
    Operacao = (input('Selecione a opção operação:'))
    if Operacao == '+' or Operacao == '-' or Operacao == '*' or Operacao == '/':
        N1 = int(input('Digite o primeiro valor'' '))
        N2 = int(input('Digite o primeiro valor'' '))

print('Encerrando o programa')
