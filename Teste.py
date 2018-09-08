from modelo import *
import re
import random

meuCombatente = Combatente("Tharin")
meuHeroi = Heroi("Randal")
minhaCriatura = Criatura("Halabb", 23, 12)


def Converter(dados, mostraRolagem=False, vatagem=False, desvantagem=False):
    '''Converte a expressão passada para um número.
       A expressão pode ser no formato: xdy +/- z,
       onde um número x de dados tipo y serão lançados e somados.'''

    dados = str(dados)
    dados = re.sub(
        r"d(\d+)", r"*rolar(\1, vatagem, desvantagem, mostraRolagem)", dados)

    resultado = eval(dados)

    if mostraRolagem:
        print(
            "Expressão: {dados} -> Resultado: {resultado}".format(dados=dados, resultado=resultado))

    return resultado


def rolar(numeroDado, vantagem=False, desvantagem=False, mostraRolagem=False):
    '''Retorna um número inteiro aleatório entre 1 e o número passado.'''

    rolagem1 = random.randint(1, int(numeroDado))
    rolagem2 = random.randint(1, int(numeroDado))

    if vantagem:
        resultado = max(rolagem1, rolagem2)
    elif desvantagem:
        resultado = min(rolagem1, rolagem2)
    else:
        resultado = rolagem1

    if mostraRolagem:
        print("Rolagem (apenas o dado): {resultado}".format(
            resultado=resultado))

    return resultado
