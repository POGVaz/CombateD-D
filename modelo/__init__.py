""" Arquivo de inicialização das classe do Modelo:

Deve conter a importação de todas as classes a serem usadas.
Também inicia o logger para os módulos deste pacote.
"""
import logging
from modelo.combatentes import *


def iniciaLogger():
    ''' Inicia as opções para o logger.
        Reunidas aqui para organização.
        Retorna o logger para ser usado pelo módulo. '''

    # Pega no nome do módulo para o logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Cria um logger para a tela:
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(levelname)-8s : %(message)s'))

    logger.addHandler(handler)

    return logger


logger = iniciaLogger()
logger.debug("Logger inicializado")
