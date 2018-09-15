import tkinter as Tk


class JanelaCombate(Tk.Tk):
    """# TODO: Escrever esta descrição """

    def __init__(self, interface):
        super(JanelaCombate, self).__init__()

        self.interface = interface

        self.title("Combate D&D")
        #self.protocol("WM_DELETE_WINDOW", self.aoFechar)

        self.menuNavegacao = MenuNavegacao(self)
        self.constroiIniciativa()
        self.constroiTabela()
        self.constroiMapa()

    def aoFechar(self, even=None):

        self.janelaDialogo = JanelaDialogo(self)

    def constroiIniciativa(self):
        pass

    def constroiTabela(self):
        pass

    def constroiMapa(self):
        pass


class JanelaDialogo(Tk.Toplevel):
    """docstring for JanelaDialogo."""

    def __init__(self, parent=None):
        super(JanelaDialogo, self).__init__(parent)
        self.parent = parent

        self.title("Fechar")

        self.labelFechar = Tk.Label(self, text='Fechando a aplicação')
        self.labelFechar.pack()

        self.botaoOk = Tk.Button(self, text='OK', command=self.fechaAplicacao)
        self.botaoOk.pack()

    def fechaAplicacao(self, event=None):

        self.destroy()
        self.parent.destroy()


class MenuNavegacao(Tk.Menu):
    """docstring for MenuNavegacao."""

    def __init__(self, parent=None):
        super(MenuNavegacao, self).__init__(parent)
        self.parent = parent

        # Primeiro dropdown "Arquivo":
        self.menuArquivo = Tk.Menu(self, tearoff=False)
        self.add_cascade(label='Arquivo', menu=self.menuArquivo)
        self.menuArquivo.add_command(
            label='Novo combate')  # ,
        # command=self.novoCombate)
        self.menuArquivo.add_command(
            label='Salvar Combate')  # ,
        # command=self.salvarCombate)
        self.menuArquivo.add_command(
            label='Carregar Combate')  # ,
        # command=self.carregarCombate)
        self.menuArquivo.add_separator()
        self.menuArquivo.add_command(label='Sair')  # , command=self.finalizar)

        # Segundo dropdown: "Combate":
        self.menuCombate = Tk.Menu(self, tearoff=False)
        self.menuCombate.add_command(label='Rolar Iniciativa')
        self.menuCombate.add_command(label='Selecionar Combatentes',
                                     command=self.aoClicarSelecaoCombatentes)
        self.menuCombate.add_separator()
        # self.
        # self.
        self.menuArquivo.add_command(label='Configurar selcionado')  # ,
        # command=self.configurarCombatente)
        self.add_cascade(label='Combate', menu=self.menuCombate)

        # Finalemnte, adiciona o menu à janela:
        self.parent.config(menu=self)

    def aoClicarSelecaoCombatentes(self):
        self.parent.interface.abrirJanelaSelecao()


class OrdemIniciativa(Tk.Frame):
    """docstring for OrdemIniciativa."""

    def __init__(self, parent=None):
        super(OrdemIniciativa, self).__init__(parent)
        self.parent = parent
