from modelo import *
from interface import *
from controlador import *


def main():
    logger = iniciaLogger()

    modelo = Modelo()
    interface = Interface(modelo=modelo)
    controlador = Controlador(interface=interface, modelo=modelo)

    logger.debug("---Inicio do loop da aplicação---")
    interface.aplicacao.mainloop()
    logger.debug("---Final do loop da aplicação---")


def iniciaLogger():
    ''' Inicia as opções para o logger.
        Reunidas aqui para organização.
        Retorna o logger para ser usado pelo módulo. '''

    FORMATO_LOG = "%(name)-12s -> %(levelname)-8s : %(message)s"
    NIVEL_LOG = logging.DEBUG

    # Pega no nome do módulo para o logger:
    logger = logging.getLogger("Main")
    logger.setLevel(NIVEL_LOG)

    # Cria um logger para a tela e define seu formato:
    handler = logging.StreamHandler()
    handler.setLevel(NIVEL_LOG)
    handler.setFormatter(logging.Formatter(FORMATO_LOG))

    logger.addHandler(handler)

    Controlador.iniciaLogger(NIVEL_LOG, FORMATO_LOG)
    Interface.iniciaLogger(NIVEL_LOG, FORMATO_LOG)
    Modelo.iniciaLogger(NIVEL_LOG, FORMATO_LOG)

    logger.info("Logger inicializado")

    return logger


main()
