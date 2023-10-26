#Calculo de média de 3 matérias, acima de 7 é aprovado.
N1 = float(input('Digite a nota final da primeira matéria :'))
N2 = float(input('Digite a nota final da segunda matéria :'))
N3 = float(input('Digite a nota final da terceira matéria :'))

NF = (N1+N2+N3) / 3

if NF >= 7:
    print('Aprovado com média {}'.format(NF))
else:
    print('Reprovado com média {}'.format(NF))

 #Aluno deve tirar média 7 nas três matérias

N = float(input('Digite a nota final da primeira matéria :'))
N0 = float(input('Digite a nota final da segunda matéria :'))
N11 = float(input('Digite a nota final da terceira matéria :'))

if N >= 7 and N0 >= 7 and N11 >= 7:
    print('Aluno aprovado!')
else:
    print('Aluno Reprovado!')