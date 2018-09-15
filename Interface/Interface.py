import logging
import tkinter as Tk

#from interface.telaPrincipal import *
from interface.janelaCombate import *
from interface.janelaSelecao import *


class Interface:
    """# TODO: Escrever Esta descrição."""

    # Referência para o Logger:
    log = None

    def __init__(self, modelo):

        # Guarda a referência para o Modelo:
        self.modelo = modelo

        self.aplicacao = Tk.Tk()
        self.aplicacao.withdraw()

        self.janelaCombate = JanelaCombate(self)

        Interface.log.debug("Instanciado")

    def inicializaInterface(self):
        '''Inicializa a janela principal da interface, organizando
           todos os frames e widgets presentes na primeira página'''

        # Cria a referência da janela principal da interface:
        self.aplicacao = JanelaCombate()

        Interface.log.debug("Inicializado")

    def abrirJanelaSelecao(self):
        '''Inicializa a janela de seleção'''

        # Cria a referência da janela principal da interface:
        self.janelaSelecao = JanelaSelecao(self)

        # Interface.log.debug("Inicializado")

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
