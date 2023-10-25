#!/usr/bin/env python3

"""Imprime a tabuada do 1 ao 10.

Script simples para praticar conceitos de tipos de dados ensinados na aula.
"""
__version__ = "0.1.0"
__author__ = "Gustavo"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterable
numeros = list(range(1, 11))

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} X {n2} = {resultado}"))
    print("#"*18)