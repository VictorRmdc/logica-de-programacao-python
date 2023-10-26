def cachorro_pelo(): # inicio da função Cachorro_pelo
    while True: # inicio do laço para que seja selecionado o pelo do cachorro.
        print('entre com o pelo do cachorro')
        print('c - pelo curto')
        print('m - pelo médio')
        print('g - pelo grande')
        pelo = input() # Aqui é a entrada da opção selecionada
        if pelo.lower() == 'c':
            return 1.0 # de acordo com a opção selecionada o valor será enviado ao programa solicitante.
        elif pelo.lower() == 'm':
            return 1.5
        elif pelo.lower() == 'g':
            return 2.0
        else:
            print('Opção incorreta. Tente novamente')# Retorno em caso onde o cliente seleciona opção não existente.

def cachorro_peso(): # inicio da função Cachorro_peso
    while True: # inicio do laço
        try:
            peso = int(input('Entre com o peso do cachorro :')) # entrada do peso do cachorro
            if peso > 0 and peso < 3:
                return 40.00
            elif peso >= 3 and peso < 10:
                return 50.00
            elif peso >= 10 and peso < 30:
                return 60.00
            elif peso >= 30 and peso < 50:
                return 70.00
            else:
                print('Não aceitamos cachorros tão grandes')
                print('Por favor entre com o peso do cachorro novamente')

        except ValueError: # Caso o cliente digite dado que não seja númerico, será orientado a colocar o dado no formato correto.
            print('Você não digitou um dado númerico')
            print('Digite o peso novamente')


def cachorro_extra(): # inicio da função Cachorro_extra
    acumulador = 0 # Acumulador se inicia valendo 0
    while True: # inicio do laço
        try:
            print('Deseja adicionar mais algum serviço ?')
            print('1 - Corte de unhas - R$ 10,00')
            print('2 - Escovar os dentes - R$ 12,00')
            print('3 - Limpeza de orelhas - R$ 15,00')
            print('0 - Não desejo mais nada')
            extra = int(input()) # entrada da opção mostrada.

            if extra == 0:
                break  # Se o cliente selecionar o opção sair, o laço será encerrado.

            elif extra == 1:
                acumulador = acumulador + 10.00
                continue # retorna ao inicio do laço.

            elif extra == 2:
                acumulador = acumulador + 12.00
                continue # retorna ao inicio do laço.

            elif extra == 3:
                acumulador = acumulador + 15.00
                continue # retorna ao inicio do laço.

            else:
                print('Opção inválida')
        except ValueError: # Caso o cliente digite dado que não seja númerico, será orientado a colocar o dado no formato correto.
            print('Valor digitado não compativel')
    return acumulador # Após o cliente selecionar a saída, será retornado o valor acumulado ao programa principal.


# Programa principal
#Inicio do main

print('Bem vindo ao Pet Shop Victor Hugo Miranda Carneiro')
peso = cachorro_peso() # Variavel do programa principal recebendo informações da função;
pelo = cachorro_pelo() # Variavel do programa principal recebendo informações da função;
extra = cachorro_extra() # Variavel do programa principal recebendo informações da função;
total = peso * pelo + extra # Variavel do programa principal recebendo informações da função;

print('Total a pagar R$ {:.2f} (peso: {:.0f} * pelo: {} + adicional(is): {:.2f})'.format(total, peso, pelo, extra)) # Saída das informações de acordo com a seleção do cliente.
