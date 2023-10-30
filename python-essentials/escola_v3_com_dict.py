#!/usr/bin/env python3
"""Exibe relatório de alunos por atividade

Imprimir a lista de alunos agrupadas por sala que frequentam cada uma das atividades.
"""

__version__ = "0.1.2"

# Dados

salas = {
    "sala_1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala_2": ["João", "Antonio", "Carlos", "Maria", "Isolda"]
}

aulas = {
    "aula_ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "aula_musica": ["Erik", "Carlos", "Maria"],
    "aula_danca": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

atividades = {
    "Inglês": aulas['aula_ingles'], 
    "Música": aulas['aula_musica'], 
    "Dança": aulas["aula_danca"]
    }

# Listar alunos em cada atividade por sala

for nome, atividade in atividades.items():

    print(f"Alunos da atividade {nome}")
    print("-" * 40)


    #  Salas que tem interseção com a atividade
    atividade_sala1 = set(salas["sala_1"]) & set(atividade)
    atividade_sala2 = set(salas["sala_2"]) & set(atividade)

    print("Sala 1", atividade_sala1)
    print("Sala 2", atividade_sala2)
    print()
    print("#" * 40)
