import tkinter as Tk


class JanelaSelecao(Tk.Toplevel):
    """# TODO: Escrever esta descrição """

    def __init__(self, interface):
        super(JanelaSelecao, self).__init__()

        self.interface = interface

        self.title("Seleção de Combatentes")
        #self.protocol("WM_DELETE_WINDOW", self.aoFechar)

        self.frameHerois = FrameHerois(self)
        self.frameHerois.grid(row=0, column=0, sticky=W+E+N+S)

        self.frameCriatura = FrameCriatura(self)
        self.frameCriatura.grid(row=0, column=0, sticky=W+E+N+S)


class FrameHeroi(Tk.Frame):
    """ """

    def __init__(self, parent=None):
        super(FrameHeroi, self).__init__(parent)
        self.parent = parent

    def fechaAplicacao(self, event=None):

        self.destroy()
        self.parent.destroy()


class FrameCriatura(Tk.Frame):
    """ """

    def __init__(self, parent=None):
        super(MenuNavegacao, self).__init__(parent)
        self.parent = parent


class OrdemIniciativa(Tk.Frame):
    """docstring for OrdemIniciativa."""

    def __init__(self, parent=None):
        super(OrdemIniciativa, self).__init__(parent)
        self.parent = parent
