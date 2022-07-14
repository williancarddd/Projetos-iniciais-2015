import tkinter
import tkinter.messagebox
from classes import  menu_bt_direito
from variaveis import variaveis
from classes import api_requestT



class Meu_Cep(object):
    def __init__(self, master):
        self.master = master

        #configurações
        self.master.option_readfile(variaveis.option_db_stylesheet, 10)  #tema de cores
        self.copycut = menu_bt_direito.Class_menu() # menur copiar colar
        self.copycut.make_menu(self.master) # cria menu de opçoes copy cut paste
        self.master['bg'] = '#383932'
        self.stringvars = tkinter.StringVar()
        self.stringvars.trace('w', self.limiteEntradaCep)


        # IMAGENS
        self.Seta_foto = tkinter.PhotoImage(file='E:\Meu_Cep\imagens\\next.png')


        #criar objetos na tela
        self.__Buscar_cep = tkinter.Entry(self.master, width=20, textvariable=self.stringvars) #entry
        self.__Buscar_cep.bind_class("Entry",'<Button-3><ButtonRelease-3>',self.copycut.show_menu) #configurar menu no entry
        #menu_bt_direito.FistClick(self.__Buscar_cep, 'Seu Cep') # mensagem de fundo
        self.__Buscar_cep.place(x=130, y=30)

        self.__Imagem_seta = tkinter.Button(self.master, image=self.Seta_foto, relief=tkinter.SOLID, activebackground='#6A7F6D', command=self.informarDados) #botao
        self.__Imagem_seta.image = self.Seta_foto # referencia para foto nao sumir
        self.__Imagem_seta.place(x=335, y=26, width=100)

        self.__informacao = tkinter.Text(self.master,width=40,height=20, relief=tkinter.FLAT) # saida de informaçao
        self.__informacao.place(x=50,y=70)

        self.__informacao.insert(1.0,f'hello world')

    def limiteEntradaCep(self, *string):
        value = self.stringvars.get()
        if len(value) > 8:
            self.stringvars.set(value[:8])

    def informarDados(self,arg=None):
        cep = self.__Buscar_cep.get()
        self.__informacao.delete(1.0, tkinter.END)

        import _thread
        from DB_dataBase import Db_class
        if cep.isdecimal():
            #nao converter numero para int porque o python remove o 0 da frente
            _thread.start_new_thread(api_requestT.api_requests, (self.__informacao, cep))
            db = Db_class.DataBase()
            print(cep)
        else:
            print('debug::::::::::::::', cep)


        #self.__Buscar_cep.delete(0, tkinter.END)
