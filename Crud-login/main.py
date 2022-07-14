import Painel
from tkinter import *


janela = Tk()
Painel.Programa(janela)

#janela.minsize(width=400,height=400)
#janela.maxsize(width=400,height=400) # define tamanha maximo que a janela pode ser redimesionavel
janela.wm_iconbitmap('icone-do-topo.ico')
janela.resizable(0,0) # desativa maxizaçao
janela.geometry('400x400+250+250')
janela.mainloop()