import pymongo
import logging


class Modelo:
    """# TODO: Escrever esta descrição."""

    # Logger:
    log = None

    def __init__(self):

        # Logger:
        Modelo.log.debug("Instanciado")

        meuCliente = pymongo.MongoClient("mongodb://localhost:27017/")
        combateBD = meuCliente["combateBD"]

        colecaoHerois = combateBD["herois"]

        meuHeroi = {"nome": "Tharin", "vida": 30}

        colecaoHerois.insert_one(meuHeroi)

        dblist = meuCliente.list_database_names()
        if "combateBD" in dblist:
            print("A base de dados foi criada!")

        Modelo.log.debug("Base de dados carregada")

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
