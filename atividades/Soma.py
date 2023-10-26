# Exercício de soma
# Exercício de soma
n1 = int(input('Digite um número : '))
n2 = int(input('Digite outro Número : '))

# Maneira clássica
res = 'O resultado da Soma de %i com %i e %i.' % (n1, n2, n1 + n2)
print(res)

# Maneira moderna
res = 'O resutado da soma de {} com {} e {}.'.format(n1, n2, n1 + n2)
print(res)