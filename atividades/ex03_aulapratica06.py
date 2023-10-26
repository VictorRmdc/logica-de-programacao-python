# Cadastro de informações no dicionario cadastro.
cadastro = {'nome': [], 'sexo': [], 'ano': []}

while True:
    terminar = input('Deseja cadastrar uma pessoa ? [S/N] :')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO')
        continue

    nome = input('Digite o nome? ')
    sexo = input('Qual é o sexo ? [M/F] ')
    ano = int(input('Qual é o ano de nascimento? '))

    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)