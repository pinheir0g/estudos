"""Algoritmo para dizer se é um triangulo válido e qual o seu tipo:
Equilátero — Todos os lados iguais
Isósceles — Pelo menos um lado diferente
Escaleno — Todos os lados diferentes
"""
# Entrada dos dados
l1 = int(input('L1: '))
l2 = int(input('L2: '))
l3 = int(input('L3: '))

# Verifica se é uma triangulo válido
if l1 > 0 and l2 > 0 and l3 > 0:
    if l1 + l2 >= l3 and l1 + l3 >= l2 and l2 + l3 >= l1:

        # Verifica qual tipo do triangulo
        if l1 == l2 == l3:
            print('Triangulo Equilátero')
        elif l1 == l2 or l2 == l3:
            print('Triangulo Isósceles')
        else:
            print('Triangulo Escaleno')

    else:
        print('1 lado maior q a soma dos outros 2')
else:
    print('Um triangulo não pode ter um dos lados de tamanho 0!')
