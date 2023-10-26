#inicio de Variavel global
lista_colaboradores = []
id_colaboradores = 0
#fim de Variavel global


#Ininio de cadastrar_colaborador
def cadastrar_coloborador(id):
    print('Bem vindo ao cadastramento de colaboradores')
    nome = input('Nome do colaborador:')
    setor = input('Setor do colaborador:')
    pagamento = int(input('Pagamento do coloborador:'))
    dicionario_colaboradores = {'id' : id, 'nome' : nome, 'setor' : setor,  'pagamento' : pagamento }

    lista_colaboradores.append(dicionario_colaboradores.copy())#Realizando uma copia do dicionario coloboradors para a lista colaboradores
#Fim de cadastrar_colaborador

#Ininio de consultar_colaborador
def consultar_coloborador():
    while True: # inicio do laço
        try:
            print('Bem vindo a consulta de colaboradores')
            opcao_consulta = int(input('1 - Consultar todos\n'
                                   '2 - Consultar por ID\n'
                                   '3 - Consultar por setor\n'
                                   '4 - Retornar ao menu\n'+
                                   '>>'))
            if opcao_consulta == 1:
                print('Você escolheu a opção de consulta de todos os colaboradores')
                for colaborador in lista_colaboradores: # Produto vai trazer toda a lista de colaboradores
                    print('-----------------------------')
                    for key, value in colaborador.items(): # trazer todos os conjuntos do dicionario colaborador
                        print('{} : {}'.format(key,value))
                    print('-----------------------------')
            elif opcao_consulta == 2:
                print('Você escolheu a opção de consulta por ID')
                id = int(input('Entre com o ID do colaborador: '))
                for colaborador in lista_colaboradores:
                    if colaborador ['id'] == id: # O valor do id solicitado é igual ao cadastrado no dicionario
                        print('-----------------------------')
                        for key, value in colaborador.items():  # trazer todos os conjuntos do dicionario colaborador
                            print('{} : {}'.format(key, value))
                        print('-----------------------------')
            elif opcao_consulta == 3:
                print('Você escolheu a opção de consulta por setor')
                setor = input('Selecione o setor: ')
                for colaborador in lista_colaboradores:
                    if colaborador ['setor'] == setor: # Verificando se o valor do setor solicitado é igual ao cadastrado no dicionario
                        print('-----------------------------')
                        for key, value in colaborador.items():  # trazer todos os conjuntos do dicionario colaborador
                            print('{} : {}'.format(key, value))
                        print('-----------------------------')
            elif opcao_consulta == 4:
                return # Sai da função de consultar coloborador e retorna ao programa principal main
            else:
                print('Opção inválida')

        except ValueError: # Caso o cliente digite dado que não seja númerico, será orientado a colocar o dado no formato correto.
            print('Você não digitou um dado númerico\n' +
                  'Digite novamente')


#Fim de consultar_colaborador

#Ininio de remover_colaborador
def remover_coloborador():
    print('Bem vindo ao removedor de colaboradores')
    id = int(input('Digite o ID do colaborador que deseja remover: '))
    for colaborador in lista_colaboradores:
        if colaborador['id'] == id:  # Verificando se o valor do id solicitado é igual ao cadastrado no dicionario para seguir com a remoção
            lista_colaboradores.remove(colaborador)#Remove o colaborador com o id solicitado.
            print('Colaborador Removido!')

#Fim de remover_colaborador

# Programa principal, Main.
print('Bem vindo ao controle de colaboradores do Victor Hugo Miranda Carneiro')
while True:
    try:
        opcao_principal = int(input('Escolha a opção desejada\n'+
                            '1 - Cadastrar colaborador\n'+
                            '2 - Consultar colaborador\n'+
                            '3 - Remover colaborador\n'+
                            '4 - Encerrar programa\n'+
                                    '>>'))
        if opcao_principal == 1:
            id_colaboradores = id_colaboradores + 1
            cadastrar_coloborador(id_colaboradores)

        elif opcao_principal == 2:
            consultar_coloborador()

        elif opcao_principal == 3:
            remover_coloborador()

        elif opcao_principal == 4:
            break # Encerra o laço principal
        else:
            print('Opção invalida')
            continue # volta para o inicio do laço.
    except ValueError: # Caso o cliente digite dado que não seja númerico, será orientado a colocar o dado no formato correto.
        print('Você não digitou um dado númerico\n'+
              'Digite novamente')
