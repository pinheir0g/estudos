#!/usr/bin/env python3

"""Hello World Multi Languages

Depending on the language configured in the environment, the program displays the corresponding message.

How to use:
Have the LANG variable properly configured 
Ex:
    export LANG=pt_BR

Or enter the CLI argument `--lang=`

Or the user has to type it in.

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
    try:
        key, value = arg.split("=")
    except ValueError as e:
        # TODO: Utilizar logging
        print(f"[ERROR] {str(e)}")
        print("You need to use `=`")
        print(f"You passed {arg}")
        print("Try with --key=value")
        sys.exit(1)

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

#  EAFP
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid choose from: {list(msg.keys())}")
    sys.exit(1)

print(
    message * int(arguments["count"])
    )
