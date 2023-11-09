#!/usr/bin/env python3

import os
import logging

# BOILERPLATE (codigo repetitivo)
# TODO: usar função
# TODO: usar lig (loguru)

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# nossa instancia
log = logging.Logger("Logs.py", log_level)
# level
ch = logging.StreamHandler()    # Console/terminal/stderr
ch.setLevel(log_level)
# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execução")
log.critical("Erro geral ex: banco de dados sumiu")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro: %s", str(e))