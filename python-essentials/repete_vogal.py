"""Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma das palavras com suas vogais duplicadas.

ex:
python repete_vogal.py
'Digite uma palavra (ou enter para sair): ' Python
'Digite uma palavra (ou enter para sair): ' Curso
'Digite uma palavra (ou enter para sair): ' <enter>

Pythoon
Cuursoo
"""

words = []
while True:
    word = input("Type a word (or enter to exit): ").strip()
    if not word:
        break

    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        if letter.lower() in 'aeiouãêóíá':
            final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)

print(*words, sep='\n')