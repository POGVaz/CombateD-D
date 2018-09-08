""" Combatentes:

Este modulo contem todas as classe relacionadas aos combatentes de um determinado combate.
# TODO: Completar esta descrição.
"""

import logging

# Logger:
log = logging.getLogger(__name__)


class Combatente:
    '''Superclasse para todos envolvidos em combate.'''

    quantidade = 0
    lista = []

    def __init__(self, nome, classeArmadura=10):
        self.nome = nome
        self.classeArmadura = classeArmadura

        Combatente.quantidade += 1
        Combatente.lista.append(self)

        log.debug("Combatente criado")

    @classmethod
    def mostra(cls):
        '''Mostra todos os combatentes da lista.
           Varia com a classe que chamou este método.'''

        for combatente in cls.lista:
            log.info(combatente.nome)
            log.debug(combatente)
            log.debug(combatente.classeArmadura)


class Heroi(Combatente):
    '''# TODO: Completar esta descrição.'''

    quantidade = 0
    lista = []

    def __init__(self, nome, classeArmadura=10):
        super(Heroi, self).__init__(nome)

        Heroi.quantidade += 1
        Heroi.lista.append(self)

        log.debug("Heroi criado")

    def CriarHerois(lista, arquivo):
        ListaHerois = []
        with open(arquivo + '.txt')as arquivo:
            for heroi in lista:
                arquivo.seek(0)
                for linha in arquivo:
                    linha = linha.split()
                    if heroi in linha:
                        ListaHerois.append(Heroi(linha[0], linha[1]))
        return ListaHerois


class Criatura(Combatente):
    '''# TODO: Completar esta descrição.'''

    quantidade = 0
    lista = []

    def __init__(self, nome, vida, classeArmadura):
        super(Criatura, self).__init__(nome)

        Criatura.quantidade += 1
        Criatura.lista.append(self)

        log.debug("Criatura criado")

    def CriarCriaturas(lista, arquivo):
        listaCriaturas = []
        with open(arquivo + '.txt') as arquivo:
            for criatura in lista:
                arquivo.seek(0)
                for linha in arquivo:
                    linha = linha.split()
                    if criatura[0] in linha:
                        for i in range(int(criatura[1])):
                            listaCriaturas.append(
                                Criatura(linha[0]+str(i), linha[1], linha[2]))
        return listaCriaturas
