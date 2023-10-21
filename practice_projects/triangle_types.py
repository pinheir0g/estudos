#!/usr/bin/env python3

"""Types of Triangles
Algorithm to tell if it is a valid triangle and what type it is:
Equilateral - All sides equal
Isosceles - At least one side different
Scalene - All sides different
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
