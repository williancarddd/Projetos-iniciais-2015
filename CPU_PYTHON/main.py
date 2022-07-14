from Modules import InterfaceMain
from Constants import variables

if __name__ == '__main__':
    root = InterfaceMain.tkinter.Tk() # JANELA PRINCIPAL
    root.wm_iconbitmap(variables.ICON_1)
    root.title(variables.TITLE) # TITULO
    root.geometry(variables.GEOMETRY) # GEOMETRIA DA JANELA
    root.resizable(False, False) # DESATIVA A EDIÇÃO DO TAMANHO DA JANELA
    InterfaceMain.MainCreator(root)  # INSTANCIA DO PROGRAMA PRINCIPAL
    root.mainloop() # INICIA O PROGRAMA

