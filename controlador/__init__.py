""" Arquivo de inicialização das classe de Controlador:

Deve conter a importação de todas as classes a serem usadas.
Também inicia o logger para os módulos deste pacote.
"""

import logging
from controlador.rolagemDados import *


def iniciaLogger():
    ''' Inicia as opções para o logger.
        Reunidas aqui para organização.
        Retorna o logger para ser usado pelo módulo. '''

    # Pega no nome do módulo para o logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Cria um logger para a tela e define seu formato:
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(levelname)-8s : %(message)s'))

    logger.addHandler(handler)

    logger.debug("Logger para {modulo} inicializado".format(modulo=__name__))

    return logger


logger = iniciaLogger()
