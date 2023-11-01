#!/usr/bin/env python3

"""Hello World Multi Languages

Depending on the language configured in the environment, the program displays the corresponding message.

How to use:
Have the LANG variable properly configured 
Ex:
    export LANG=pt_BR

Ou informe atraves do CLI argument `--lang=`

Ou o usuário terá que digitar.

Execution:
    python3 hello.py
"""
__version__ = "0.1.3"
__author__ = "Gustavo Pinheiro"
__license__ = "Unlicense"

import os
import sys


arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
     # TODO: Tratar ValueError

    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid Option: `{key}`")
        sys.exit()

    arguments[key] = value


current_language =  arguments["lang"]

if current_language is None:
    # TODO: Usar repetição
    
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {"en_US": "Hello, World!",
       "pt_BR": "Olá Mundo!",
       "it_IT": "Ciao Mondo!",
       "es_SP": "Hola, Mundo!",
       "ja_JP": "Konnichiwa, Sekai!",
       "fr_FR": "Bonjou, Monde!",
       "mn_MN": "Sain baina uu, delkhi!",
       "zh_CN": "Nǐ hǎo, shìjiè!"
       }

#  O(1) - constante
print(
    msg[current_language] * int(arguments["count"])
    )
