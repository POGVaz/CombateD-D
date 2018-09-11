import logging
from tkinter import *

# Logger:
log = logging.getLogger(__name__)


class Aplicacao:
    def __init__(janela, master=None):

        janela.topCombate = Toplevel()
        janela.topCombate.title("Combate D&D")
        janela.topCombate.protocol("WM_DELETE_WINDOW", janela.finalizar)

        # Criando o menu de opções da tela principal
        janela.menubar = Menu(janela.topCombate)
        janela.menuArquivo = Menu(janela.menubar, tearoff=False)
        janela.menuArquivo.add_command(
            label='Novo combate',
            command=janela.novoCombate)
        janela.menuArquivo.add_command(
            label='Salvar Combate',
            command=janela.salvarCombate)
        janela.menuArquivo.add_command(
            label='Carregar Combate',
            command=janela.carregarCombate)
        janela.menuArquivo.add_separator()
        janela.menuArquivo.add_command(label='Sair', command=janela.finalizar)
        janela.menubar.add_cascade(label='Arquivo', menu=janela.menuArquivo)
        janela.menuCombate = Menu(janela.menubar, tearoff=False)
        janela.menuCombate.add_command(label='Rolar Iniciativa')
        janela.menuCombate.add_command(label='Selecionar Combatentes',
                                       command=janela.gerarTopListas)
        janela.menuCombate.add_separator()
        # janela.
        # janela.
        janela.menuArquivo.add_command(label='Configurar selcionado',
                                       command=janela.configurarCombatente)
        janela.menubar.add_cascade(label='Combate', menu=janela.menuCombate)
        janela.topCombate.config(menu=janela.menubar)

        janela.frameIniciativa = Frame(janela.topCombate)
        janela.frameIniciativa.grid(row=0, column=0, columnspan=3)
        janela.labelIniciativa = Label(
            janela.frameIniciativa, text='Ordem de Iniciativa')
        janela.labelIniciativa.grid()

        janela.frameEstadoCriaturas = Frame(janela.topCombate)
        janela.frameEstadoCriaturas.grid(row=1, column=0)

        janela.frameAtacantes = Frame(janela.topCombate)
        janela.frameAtacantes.grid(row=1, column=1)

        janela.frameSelecionado = Frame(janela.topCombate)
        janela.frameSelecionado.grid(row=1, column=2)

    def novoCombate(janela):  # FIXME
        print('Novo combate requisitado')

    def salvarCombate(janela):  # FIXME
        print('Combate salvo')

    def carregarCombate(janela, arquivo=None):  # FIXME
        print('Combate carregado')

    def configurarCombatente(janela):  # FIXME
        print('Configurando')

    def atualizar(janela):  # FIXME
        print('Janela Atualizada')

    def gerarTopListas(janela):
        'Chamada para gerar a seleção de combatentes.'
        listaHerois = AtualizarLista(arquivoHerois)
        listaCriaturas = AtualizarLista(arquivoCriaturas)

        # Definindo a janela de seleção de combatentes
        janela.topListas = Toplevel()
        janela.topListas.title("Seleção de combatentes")

        # Criando o menu de opções da tela de listas [FIX ME]
        janela.menuListas = Menu(janela.topListas)
        janela.menuArquivoSel = Menu(janela.menuListas, tearoff=False)
        janela.menuArquivoSel.add_command(label='Abrir')
        janela.menuArquivoSel.add_command(label='Salvar')
        janela.menuArquivoSel.add_separator()
        janela.menuArquivoSel.add_command(
            label='Sair', command=janela.topListas.destroy)
        janela.menuListas.add_cascade(
            label='Arquivo', menu=janela.menuArquivoSel)
        janela.topListas.config(menu=janela.menuListas)

        # Ajustando os frames para que tudo ocupe a janela completa
        janela.frameHerois = Frame(janela.topListas)  # Lista de heróis
        janela.frameHerois.grid(row=0, column=0, sticky=W+E+N+S)
        janela.frameCriaturas = Frame(janela.topListas)  # Lista de Criaturas
        janela.frameCriaturas.grid(row=0, column=1, sticky=W+E+N+S)

        # Criando e Preenchendo a lista de Herois
        janela.labelHerois = Label(
            janela.frameHerois, text='Selecione os Heróis que combaterão:')
        janela.scrollHerois = Scrollbar(janela.frameHerois, orient=VERTICAL)
        janela.listaHerois = Listbox(janela.frameHerois, selectmode=MULTIPLE,
                                     yscrollcommand=janela.scrollHerois.set, exportselection=False)
        janela.scrollHerois.config(command=janela.listaHerois.yview)
        Preencher(janela.listaHerois, listaHerois)
        janela.scrollHerois.grid(row=1, column=1, sticky=N+S)
        janela.listaHerois.grid(row=1, column=0, sticky=W+E+N+S)
        janela.labelHerois.grid(row=0, column=0, columnspan=2)

        janela.updateHerois = Button(janela.frameHerois, text='Update', command=lambda Herois=AtualizarLista(
            arquivoHerois): Preencher(janela.listaHerois, Herois))
        janela.updateHerois.grid(row=2, column=0, columnspan=2, pady=10)
        janela.frameHerois.grid_columnconfigure(0, weight=1)
        janela.frameHerois.grid_rowconfigure(0, weight=1)

        # Criando e Preenchendo a lista de Criaturas
        janela.labelCriaturas = Label(
            janela.frameCriaturas, text='Selecione as criaturas que eles enfrentarão:')
        janela.labelCriaturas.grid(columnspan=3)
        janela.scrollCriaturas = Scrollbar(
            janela.frameCriaturas, orient=VERTICAL)
        janela.listaCriaturas = Listbox(janela.frameCriaturas, selectmode=MULTIPLE,
                                        yscrollcommand=janela.scrollCriaturas.set, exportselection=False)
        janela.scrollCriaturas.config(command=janela.listaCriaturas.yview)
        Preencher(janela.listaCriaturas, listaCriaturas)
        janela.entradaCriaturas = []
        for i in range(len(listaCriaturas)):
            janela.entrada = Entry(janela.frameCriaturas)
            janela.entradaCriaturas.append(janela.entrada)
            janela.entradaCriaturas[i].grid(sticky=N)
        janela.listaCriaturas.grid(
            column=1, sticky=W+E+N+S, rowspan=len(janela.entradaCriaturas))
        janela.scrollCriaturas.grid(
            column=2, sticky=N+S, rowspan=len(janela.entradaCriaturas))

        janela.updateCriaturas = Button(janela.frameCriaturas, text='Update', command=lambda Criaturas=AtualizarLista(
            arquivoCriaturas): Preencher(janela.listaCriaturas, Criaturas))
        janela.updateCriaturas.grid(column=0, columnspan=3, pady=10)
        janela.frameCriaturas.grid_columnconfigure(0, weight=1)
        janela.frameCriaturas.grid_rowconfigure(0, weight=1)

        # Botão confirma
        janela.listaConfirma = Button(janela.topListas, text='Confirmar Seleção',
                                      command=janela.confirmaSelecao, width=20, height=3, font=("Verdana", "20", "bold"))
        janela.listaConfirma.grid(row=1, column=0, columnspan=2, pady=20)
        janela.topListas.bind("<Return>", janela.confirmaSelecao)
        janela.topListas.grid_columnconfigure(0, weight=1)
        janela.topListas.grid_columnconfigure(1, weight=1)
        janela.topListas.grid_rowconfigure(0, weight=1)

    def confirmaSelecao(janela, event=None):  # [FIX ME]
        global Herois, Criaturas
        Herois[:] = []
        Criaturas[:] = []
        for Heroi in janela.listaHerois.curselection():
            Herois.append(janela.listaHerois.get(Heroi))
        Herois = Heroi.CriarHerois(Herois, arquivoHerois)
        for Criatura, Quantidade in zip(janela.listaCriaturas.curselection(), janela.entradaCriaturas):
            Criaturas.append(
                [janela.listaCriaturas.get(Criatura), Quantidade.get()])
        Criaturas = Criatura.CriarCriaturas(Criaturas, arquivoCriaturas)
        janela.topListas.destroy()
        janela.atualizar()
        print("confirma")

    def finalizar(janela, event=None):  # [FIX ME]
        janela.destroy()
        print("acabou")


def Preencher(listbox, dados):
    'Limpa uma listbox e a preenche com valores de uma lista dados.'
    listbox.delete(0, END)
    for objeto in dados:
        listbox.insert(END, objeto)


#janela = Tk()
#Aplicacao = Aplicacao(janela)
