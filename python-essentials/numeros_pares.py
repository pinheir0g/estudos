#!usr/bin/env python3
"""
Faça um programa que imprima os números pares de 1 a 200

ex
`python 3 numeros_pares.py`
2
4
6
8
...
"""
for n in range(2, 201, 2):
    print(n)

"""
for n in range(1, 201):
    if n % 2 != 0:
        continue
    print(n)
"""