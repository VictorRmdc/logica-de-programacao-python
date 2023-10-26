# calculadora
print('-----------------')
print('SELECIONE A OPERAÇÃO')
print('1 : [ + ]')
print('2 : [ - ]')
print('3 : [ * ]')
print('4 : [ / ]')
print('--------------------')
Operacao = int(input('Selecione a opção de 1 a 4 :'))
print('--------------------')

N1 = int(input('Digite o primeiro valor'' '))
N2 = int(input('Digite o primeiro valor'' '))

if Operacao == 1:
    Resultado = N1 + N2
    print('A soma de {} + {} é {}'.format(N1, N2, Resultado))
else:
    if Operacao == 2:
        Resultado = N1 - N2
        print('A Subtração de {} - {} é {}'.format(N1, N2, Resultado))
    else:
        if Operacao == 3:
            Resultado = N1 * N2
            print('A multiplicação de {} x {} é {}'.format(N1, N2, Resultado))
        else:
            if Operacao == 4:
                Resultado = N1 / N2
                print('A divisão de {} / {} é {}'.format(N1, N2, Resultado))
            else:
                print('Opção inexistente')

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
    print('Encerrando o programa')