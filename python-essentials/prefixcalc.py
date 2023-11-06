#!/usr/bin/env python3
""" Calculadora Prefix
Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> - 
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `infixcalc.log`
"""
__version__ = "0.1.0"

import sys
import os
from datetime import datetime
arguments = sys.argv[1:]

# TODO: Exceptions
if not arguments:
    operation = (input("operação: "))
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: `sum 5 5 `")
    sys.exit(1)

# Desempacotar os valores de arguments dentro das variaveis operation e nums
operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")

if operation not in valid_operations:
    print("Operação Inválida")
    print(valid_operations)
    sys.exit(1)

valid_nums = []
for num in nums:
    # TODO: Repetição while + Exceptions
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    valid_nums.append(num)

n1, n2 = valid_nums

operations = {
    "sum": n1 + n2,
    "sub": n1 - n2,
    "mul": n1 * n2,
    "div": n1 / n2
}

result = operations[operation]

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {user} - {operation},{n1},{n2} = {result}\n")

print(f"O resutlado é {result}")