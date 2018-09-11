import tkinter as Tk


class JanelaPrincipal(Tk.Tk):
    """# TODO: Escrever esta descrição """

    def __init__(self):
        super(JanelaPrincipal, self).__init__()

        self.title("Combate D&D")
        self.protocol("WM_DELETE_WINDOW", self.aoFechar)

        self.constroiMenu()
        self.constroiIniciativa()
        self.constroiTabela()
        self.constroiMapa()

    def aoFechar(self, even=None):

        self.janelaDialogo = JanelaDialogo(self)

    def constroiMenu(self):
        pass

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
