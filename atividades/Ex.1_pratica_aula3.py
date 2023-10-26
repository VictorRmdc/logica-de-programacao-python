# Ex 01 26/07/2023
A = int(input('Primeiro lado do triângulo:'))
B = int(input('Segundo lado do triângulo:'))
C = int(input('Terceiro lado do triângulo:'))

if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B + C > A) :
        # Se você chegou até aqui, é porque o triângulo é valido!
        if A != B and A != C and B!= C:
            print('Triângulo escaleno!')
        else:
            if A == B and A == C and B == C:
                print('Triângulo Equilatero!')
            else:
                print('Triângulo esósceles')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triangulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triangulo')