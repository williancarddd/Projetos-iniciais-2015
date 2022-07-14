from tkinter import *
import functools
from conectiondb import *
import tkinter.messagebox


class Programa(object):
    def __init__(self,instancia):
        self.instancia = instancia # referencia  do objeto janela
        self.instancia.title('Cliente Serve-Login') #titulo do programa
        self.chama_funcoes()
        self.msg1['text'] = "Bem Vindo"  # msg1 inicial do programa
        self.banco = Banco_De_Dados() # aqui ja cria o banco de dados e a conexao

    def chama_funcoes(self):
        """tem que ser na sequencia"""
        self.emailFunc()# cria widgets emails pra quando for remover nao da pau
        self.imagem_De_fundo()  # tem que ser chamado primeiro
        self.mensagem_topo()
        self.PG_inicial()
        self.criar_interatividade()  # chama o metodo paara criar o label

    def mensagem_topo(self):
        # mensagem do topo
        self.msg1 = Label(self.instancia, text=' ', width=20, font=('Helvetica', 15))  # mensagem principal
        self.msg1.pack(side=TOP)#place(x=100, y=0)

    def criar_interatividade(self): #interatividade com usuario menu
        # menus
        self.instancia.option_add('*tearOff', False)  # remove a barra traçada
        self.Menu = Menu(self.instancia)  # cria uma " instancia menu"
        self.Menu_itens = Menu(self.Menu)  # cria objeto de menu
        self.Menu_itens.add_command(label='Cadastro',command=self.painel_de_cadastro) #comando .add_command() adiciona labes dentro do menu
        self.Menu_itens.add_command(label='Configurações')
        self.Menu_itens.add_command(label='Pagina Inicial',command=self.PG_inicial)
        self.Menu.add_cascade(label='Menu',menu=self.Menu_itens)  # aqui cria o  menu em sí
        self.instancia.config(menu=self.Menu) # faz referencia direta para instancia sobre o menu,inicia o menu

    def PG_inicial(self):
        self.msg1['text'] = "Painel de Login"
        #remove os widgets email da tela
        self.emailFunc(2)
        # textos
        self.usuarioLabel = Label(self.instancia, text="Nome")  # cria texto nome
        self.senhLabel = Label(self.instancia, text='Senha')
        self.usuarioLabel.place(x=98, y=110) #dimensiona
        self.senhLabel.place(x=99, y=160)
        # entradas
        self.usuario = Entry(self.instancia)  # entrada 1
        self.senha = Entry(self.instancia, show="*")  # entrada 2

        self.usuario.focus_force()
        self.senha.focus_force()
        self.usuario.place(x=138, y=110)
        self.senha.place(x=138, y=160)
        # botoes
        self.botaoLogin = Button(self.instancia, text='Entrar', width='15',command=functools.partial(self.banco_dd,2))  # botao login
        self.botaoSair = Button(self.instancia, text='Sair', width='15', command=self.sair_programa)  # botao saiDA
        self.botaoSair.place(x=250, y=297)
        self.botaoLogin.place(x=23, y=298)

    def imagem_De_fundo(self): # imagem do fundo do programa
        self.backgroudim = PhotoImage(file='size400.gif') #instancia da foto
        self.backgroud_label = Label(self.instancia, image=self.backgroudim) #adiciona a ffoto a um label
        self.backgroud_label.place(x=0, y=0)

    def sair_programa(self):
        self.botaoSair['command'] = self.instancia.quit()

    def painel_de_cadastro(self):  # aqui fica configuraçao do cadastro
        #chama a funcao com entrada de email
        self.emailFunc(2)
        self.emailFunc(1)
        self.msg1['text'] = 'Painel de Cadastro'
        '''
        place_forget() remove os widgets
        da tela principal
         '''
        # remove os widgets
        self.usuario.place_forget()
       #self.botaoLogin.place_forget()#
        self.senha.place_forget()
        #cria configuraçoes cadastro
        self.cadastro_usuarioEntry = Entry(self.instancia)
        self.cadastro_senhaEntry = Entry(self.instancia,show='*')

        self.cadastro_usuarioEntry.focus_force() # isso evte de ficar clicando dentro do entry
        self.cadastro_senhaEntry.focus_force()
        self.cadastro_usuarioEntry.place(x=138, y=110)
        self.cadastro_senhaEntry.place(x=138, y=160)

        #botao login virando botao de cadastro
        self.botaoLogin['text'] = 'Cadastrar'
        self.botaoLogin['command'] = functools.partial(self.banco_dd,1) # cadastro
        '''  
        #botao cadastro
        self.botaoCadastro = Button(self.instancia)
        self.botaoCadastro['text'] = 'Cadastrar'
        self.botaoCadastro.place(x=23, y=298)
        '''
    def emailFunc(self,remove_widgets=None):
        if  remove_widgets == 2:
            self.cadastro_emailEntry.place_forget()
            self.cadastro_emaiLabel.place_forget()
        else:
            # email
            self.cadastro_emaiLabel = Label(self.instancia, text="Email:")
            self.cadastro_emailEntry = Entry(self.instancia)

            self.cadastro_emailEntry.focus_force()
            self.cadastro_emailEntry.place(x=138, y=210)
            self.cadastro_emaiLabel.place(x=98, y=210)

    def banco_dd(self,comando):
        user_get =  self.cadastro_usuarioEntry.get()
        pass_get = self.cadastro_senhaEntry.get()
        email_get = self.cadastro_emailEntry.get()
        if comando == 1: # se comando for igual a 1 ira cadastrar

            if self.banco.verifica_email(email_get) == False: # a funcao retorna True
                tkinter.messagebox.showinfo('Email existente',"email ja cadastrado :(")

            if self.banco.verifica_se_existe_usuario(user_get) == False:
                tkinter.messagebox.showinfo("Usuario existente",'Usuario ja cadastrado')
            else:
                self.botaoLogin.config(state='disable')
        if comando == 2:
            print('logado')