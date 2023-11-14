"""Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o indice de umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das condições:

temp maior que 45: ALERTA!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temo menor que 0: ALERTA: Frio extremo
"""
import sys
import logging
import os


log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("Alerta.py", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s'
    'l:%(lineno)d f:%(filename)s:  %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch) 

info = {
    "temperature": None,
    "humidity": None
}

for key in info.keys():
    try:
        info[key] = float(input(f"Current {key}? ").strip())
    except ValueError:
        log.error(f"Invalid {key.capitalize()}")
        sys.exit(1)

temp = info['temperature']
humid = info["humidity"]

if temp > 45:
    print("WARNING!!! Danger extreme heat")
elif temp * 3 >= humid:
    print("WARNING Danger of humid heat")
elif 10 <= temp <= 30:
    print("Normal")
elif 0 <= temp < 10:
    print("Cold")
elif temp < 0:
    print("Extreme Cold")
    