from interface import *
from controlador import *
from modelo import *

main():
    logger = iniciaLogger()

    modelo = Modelo(logger=logger)
    interface = Interface(modelo=modelo, logger=logger)
    controlador = Controlador(interface=interface, modelo=modelo, logger=logger)

    log.debug("Loop principal iniciado")
    interface.janela.withdraw()
    interface.janela.mainloop()
    log.debug("Loop principal finalizado")


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

    logger.debug("Logger inicializado")

    return logger


main()
