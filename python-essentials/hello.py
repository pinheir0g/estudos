#!/usr/bin/env python3

"""Hello World Multi Languages

Depending on the language configured in the environment, the program displays the corresponding message.

How to use:
Have the LANG variable properly configured 
Ex:
    export LANG=pt_BR

Execution:
    python3 hello.py
"""
__version__ = "0.1.2"
__author__ = "Gustavo Pinheiro"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

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
print(msg[current_language])
