import tkinter as tk
import tkinter.messagebox
from programa import  variaveis
from programa.create_widget import *

class Main_bin(object):
    def __init__(self, master):
        self.master = master
        self.master['bg'] = variaveis.COR1 # background
        '''
            funçao principal do programa
            obs:inicializadora
        '''
        #cria os frames
        self.frame1 = tk.Frame(master,bg=variaveis.COR1,pady=10)
        self.frame2 = tk.Frame(master,bg=variaveis.COR1,pady=10)
        self.frame3 = tk.Frame(master,bg=variaveis.COR1,pady=2)
        self.frame4 = tk.Frame(master,bg=variaveis.COR1)
        #empacotar widgets
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack(side=LEFT)

        # criar sobre o criador
        self.sobre = Button(self.frame1,text='Sobre o criador', command=self.func_sobre,bg=variaveis.COR4
                            ,activebackground=variaveis.COR3,fg=variaveis.COR2)
        self.sobre.pack(side=LEFT)

        #executar
        Image_wid(self.frame1, variaveis.IMAGEM_TOPO)  # classe de imagem topo
        Create_widget(self.frame2, self.frame3, self.frame4) #cria widgets na tela

    def func_sobre(self):
        tkinter.messagebox._show('Sobre o Criador',variaveis.SOBRE)

class Image_wid(object):
    '''
    adiciona imagem á um frame
    '''
    def __init__(self,master,file=None):
        self.photo = tk.PhotoImage(file=file) # recebe o caminho da imagem
        self.lbfoto = tk.Label(master, bg=variaveis.COR1, fg=variaveis.COR2, font=(variaveis.FONTE1, 13), width=560,
                               text=variaveis.TEXTO1, compound=tk.BOTTOM) #label  da imagem
        self.lbfoto.image = self.photo  # mantem referencia a o objeto imagem
        self.lbfoto.configure(image=self.photo)  # configura a imagem
        self.lbfoto.pack()