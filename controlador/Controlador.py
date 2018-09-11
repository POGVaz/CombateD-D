import logging


class Controlador:
    """# TODO: Escrever esta descrição."""

    # Logger:
    log = None

    def __init__(self, interface, modelo):

        self.modelo = modelo
        self.interface = interface

        Controlador.log.debug("Instanciado")

        interface.inicializaInterface()

    @classmethod
    def iniciaLogger(cls, nivel=logging.DEBUG, formato="%(name)-12s : %(levelname)-8s : %(message)s"):
        ''' Inicia as opções para o logger.
            Reunidas aqui para organização.
            Retorna o logger para ser usado pelo módulo. '''

        # Pega no nome do módulo para o logger:
        logger = logging.getLogger(cls.__name__)
        logger.setLevel(nivel)

        # Cria um logger para a tela e define seu formato:
        handler = logging.StreamHandler()
        handler.setLevel(nivel)
        handler.setFormatter(logging.Formatter(formato))

        logger.addHandler(handler)

        logger.debug("Logger inicializado")

        cls.log = logger
