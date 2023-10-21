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
__version__ = "0.0.1"
__author__ = "Gustavo Pinheiro"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "ja_JP":
    msg = " Konnichiwa, Sekai (こんにちは、世界)"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjou, Monde!"
elif current_language == "zh_CN":
    msg = "Nǐ hǎo, shìjiè! (你好，世界！)"
elif current_language == "mn_MN":
    msg = "Sain baina uu, delkhi! (Сайн байна уу, дэлхий!)"

print(msg)
