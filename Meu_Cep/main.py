from classes.Meu_cep_interface import *
from variaveis import variaveis


if __name__ == '__main__':
    root = tkinter.Tk()  #instancia tkinter
    root.geometry(variaveis.GEOMETRY)  #geometria
    root.resizable(False, False)  #deixar pagina imutavel
    root.wm_iconbitmap(variaveis.ICONE_TOPO)  #icone topo
    root.title(variaveis.TITLE)  #titulo
    Meu_Cep(root)  #programa principal
    root.mainloop()  #inicia
