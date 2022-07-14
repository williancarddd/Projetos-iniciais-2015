import os
import sys
import  tkinter.ttk
import tkinter.messagebox
import  psutil
import  subprocess
import ctypes
from tkinter import *
from class_menu import menuco
from variaveisproject import *
from functools import partial
from config_banco import banco_cf
from time import  sleep,localtime

class Main(object):
    '''
    essa é a classe principal do programa ClearBooster
    ela cria é define funçoes
    '''
    def __init__(self,root):
        self.root1 = root
        self.root1['bg'] = preto_meioclaro #verde_florescente
        self.frameMSG = Frame(root, bg=preto_meioclaro)
        self.frameL1  = Frame(root, bg=preto_meioclaro)
        self.frameL2  = Frame(root, bg=preto_meioclaro)
        self.frameBT  = Frame(root, bg=preto_meioclaro)
        self.list_name_objects = ['Painel de Entrada','Painel de Cadastro']

        #variaveis
        self.qtdclicks = 0
        self.nomeuser = ''

        #criar: menu
        self.root1.option_add('*tearOff',False)# tira as barras traçadas
        self.Menu = Menu(self.root1)
        self.Menu_itens = Menu(self.Menu, bg=verde_florescente,activebackground=azul_modificado)
        self.Menu_itens.add_command(label='Login',command=self.func_Login)
        self.Menu_itens.add_command(label='Cadastrar',command=self.func_cadastrar)
        self.Menu_itens.add_separator()  # separador
        self.Menu_itens.add_command(label='Ajuda',command=self.func_ajuda)
        self.Menu_itens.add_command(label='Sair',command=self.func_sair)
        self.Menu.add_cascade(label='Menu',menu=self.Menu_itens)# cria o nome Menu la em cima
        self.root1.config(menu=self.Menu,cursor='plus')

        #criar: adiciona a mensagem ao topo
        self.labelmsg = Label(self.frameMSG,text=self.list_name_objects[0],bg=preto_meioclaro,font=(FONTElabe,TamanhoFG+3),bd=8)
        self.labelmsg.pack()
        #criar: botao
        self.buttonUni = Button(self.frameBT,text='Entrar',font=(FONTElabe,TamanhoFG),bd=5,bg=preto_meioclaro, fg=verde_florescente)
        self.buttonUni.grid(row=0, column=0)
        #empacotar
        self.frameMSG.pack(pady=Pdx)
        self.frameL1.pack(pady=Pdx)
        self.frameL2.pack(pady=Pdx)
        self.frameBT.pack(pady=Pdx)
        #chama funçao
        self.buttonUni['command'] = partial(self.func_logica_De_cadastro_e_login, 1) #tem que chamar porque o painel de login sempre é,
        self.labelmsg['fg'] = azul                                                   #chamado primeiro.
        self.criar_painel()
        #criar menu copiar e colar
        self.cutcopypaste = menuco.Class_menu()
        self.cutcopypaste.make_menu(self.root1)
        self.entry1.bind_class('Entry',"<Button-3><ButtonRelease-3>",self.cutcopypaste.show_menu)

    def func_logica_De_cadastro_e_login(self, escolha):
        self.qtdclicks += 1  # soma  +1 cada vez que o botao e precionado
        self.instancia_do_banco = banco_cf.CFB()
        getnome  = self.entry1.get(); getnome.upper().strip()
        getsenha = self.entry2.get(); getsenha.upper().strip()

        if (self.qtdclicks >= 4):
            self.qtdclicks = 0
            self.buttonUni.config(state='disable') # antes do looping desativa
            for tempsecods in range(1,6):
                self.labelmsg['text'] = f'Bloqueado temporariamente {tempsecods}'
                self.root1.update();sleep(1)
            self.buttonUni.config(state="active") #depois do looping ativar

        if (escolha == 1):#vai entrar na conta
            '''
            varifica se a consulta no banco for verdadeira,
            caso for irar entrar e limpar os dados do campo é
            quantidades de clicks vai para 0
            '''
            if self.instancia_do_banco.consultar_dados(getnome,getsenha): # true
                self.qtdclicks = 0
                self.entry1.delete(0,END)
                self.entry2.delete(0, END)
                self.nomeuser = getnome
                self.criar_area_de_limpezaAPP()# chama o programa principal
            else:
                """
                exibe a mensagem se o usuario não existir
                """
                self.labelmsg['text'] = 'Usuario ou Senha estão incorretos.'

        if (escolha == 2):
            """
            Aqui tem algumas condiçoes para o cadastro no app
            """
            if getnome == '' or getsenha == '':self.labelmsg['text'] = 'Preencha todos os campos.'
            elif len(getnome) < 4: self.labelmsg['text'] = 'O nome não pode ser menor que 4\ncaracteres.'
            elif len(getnome) > 100: self.labelmsg['text'] = 'Limite de Bufer Atingido'
            elif len(getsenha) < 5: self.labelmsg['text'] = 'A senha é muita curta.'

            else:
                cadastro = self.instancia_do_banco.inserir_dados(getnome, getsenha)
                if cadastro == False:
                    self.labelmsg['text'] = 'Usuario ja cadastrado';self.labelmsg['fg'] = vermelho
                else:
                    self.labelmsg['text'] = 'Perfil cadastrado com susseco';self.labelmsg['fg'] = verde_florescente

    def criar_painel(self):
        '''
        Aqui cria os labels é entradas da tela principal do programa
        :return: None
        '''
        #Criar: Label
        self.label1 = Label(self.frameL1, text='Nome :', font=(FONTElabe, TamanhoFG), bg=preto_meioclaro)
        self.entry1 = Entry(self.frameL1, fg=azul, font=(FONTElabe, TamanhoFG))
        self.label2 = Label(self.frameL2, text='Senha:', font=(FONTElabe, TamanhoFG), bg=preto_meioclaro)
        self.entry2 = Entry(self.frameL2, fg=azul, show="*", font=(FONTElabe, TamanhoFG))
        self.label1.grid(row=1, column=1)
        self.entry1.grid(row=1, column=2)
        self.label2.grid(row=2, column=1)
        self.entry2.grid(row=2, column=2)
        #focus force
        self.entry1.focus_force()
        self.entry2.focus_force()

        self.entry1.insert(END,'admin')
        self.entry2.insert(END,'admin')

    def criar_area_de_limpezaAPP(self):
        self.root1.title('Aréa de Limpeza')
        self.func_apagarWID1()     #apaga uns widgets
        self.func_apagarWID2()     #também apaga
        self.Menu_itens.entryconfig("Login", state=DISABLED) #desativa essas opçoes do menu
        self.Menu_itens.entryconfig("Cadastrar",state=DISABLED)
        #criar label
        self.msgstate = Label(self.root1, text=f'Usuario: {self.nomeuser}',bg=preto_meioclaro,fg=verde_florescente,font=(FONTElabe,TamanhoFG-2))
        self.msgstate.place(x=0,y=0)
        #chamar os botoes de limpeza
        self.criar_menu_de_limpeza()
        #cria eventos nos botões
        self.criar_textoDElogs()
        self.criar_eventos()
        #chama a barra de progresso
        self.criar_barraDeprogresso()


    def criar_menu_de_limpeza(self):
        '''
        Aqui cria os botoes da area de limpeza.
        adiciona os botoes é imagens
        :return: None
        '''
        #icones dos botoes
        self.foguetes = []
        for i in range(1,4):
            self.foguetes.append(PhotoImage(file=f'imagens{os.sep}foguete{i}.gif'))

        self.Limpezacompleta = Button(self.root1, text='LIMPEZA COMPLETA', font=(FONTElabe, TamanhoFG),bg=branco, bd=2, fg=preto_meioclaro,width=160,height=49,image=self.foguetes[0], compound=BOTTOM,command=self.func_limpezacompleta)
        self.Limpezasimples = Button(self.root1, text='LIMPEZA SIMPLES', font=(FONTElabe, TamanhoFG), bg=branco, bd=2,fg=preto_meioclaro, width=160, height=49, image=self.foguetes[1], compound=BOTTOM,command=self.func_limpezasimples)
        self.LimpezaRapida = Button(self.root1, text='LIMPEZA RÁPIDA', font=(FONTElabe, TamanhoFG), bg=branco, bd=2,fg=preto_meioclaro, width=160, height=49, image=self.foguetes[2], compound=BOTTOM,command=self.func_limpezarapida)
        #empacotar
        self.Limpezacompleta.place(x=0,y=27)
        self.Limpezasimples.place(x=0,y=85)
        self.LimpezaRapida.place(x=0,y=143)


    def criar_textoDElogs(self):
        '''
        Cria a Area que aparece as mensagens para o usuario
        :return: None
        '''
        self.text = Text(self.root1,cursor='arrow',width=30,height=15)
        self.text1 = Text(self.root1,cursor='arrow',width=33,height=4)
        self.text.insert(END, 'Para saber como cada botao funciona passe o mouse por cima.')
        self.botaolimparlog = Label(self.root1,fg=azul_modificado,bg=preto_meioclaro,text='Limpar Logs')
        #empacotar
        self.botaolimparlog.place(x=515, y=236)#
        self.text1.place(x=0,y=210)
        self.text.place(x=270, y=10)#
        # funçao mostra info sistema
        self.func_info_do_sistema()
        #menu copiar colar para text
        self.text.bind_class('Text', "<Button-3><ButtonRelease-3>", self.cutcopypaste.show_menu)


    def criar_barraDeprogresso(self):
        '''
        cria a barra de progresso usando a clase ttk
        :return: None
        '''
        self.barprogress = tkinter.ttk.Progressbar(self.root1,mode='determinate')
        self.barprogress.place(x=270,y=256,width=245)

    def criar_eventos(self):
        '''
        cria eventos nos botoes.
        evento: quando o usuario passar o mouse por cima aparece uma mensagem no Text
        :return: None
        '''
        #mostra
        self.Limpezacompleta.bind('<Enter>', partial(self.criar_onRnter,1))
        self.Limpezasimples.bind('<Enter>', partial(self.criar_onRnter,2))
        self.LimpezaRapida.bind('<Enter>', partial(self.criar_onRnter,3))
        #apaga
        self.Limpezacompleta.bind('<Leave>', partial(self.criar_onLever,1))
        self.Limpezasimples.bind('<Leave>', partial(self.criar_onLever,2))
        self.LimpezaRapida.bind('<Leave>', partial(self.criar_onLever,3))
        #evento limpar log
        self.botaolimparlog.bind('<Button-1>',self.func_limplog)

    def criar_onRnter(self,*status):
        '''
        insere o texto quando passar o mouse
        :param status: esse '*status' é porque a funçao bind retorna uma tupla
        :return: None
        '''
        if status[0] == 1:
            self.text.insert(END,LCOMPLETA)
        if status[0] == 2:
            self.text.insert(END,LSIMPLES)
        if status[0] == 3:
            self.text.insert(END,LRAPIDA)

    def criar_onLever(self,*status):
        '''
        apaga o texto quando passar o mouse
        :param status: esse '*status' é porque a funçao bind retorna uma tupla
        :return: None
        '''
        if status[0] == 1:
            self.text.delete('1.0',END)
        if status[0] == 3:
            self.text.delete('1.0',END)
        if status[0] == 3:
            self.text.delete('1.0',END)

    def func_info_do_sistema(self):
        '''
        Mostra umas informaçoes do sistema no texto1
        RAMAT: Memoria ram atual CPU_USAGE: cpu atual do computador
        :return: None
        '''
        self.text1['bg'] = preto_meioclaro
        self.text1['fg'] = verde_florescente
        RAMAT = psutil.virtual_memory()[4]
        RAMAT = RAMAT/1024
        RAMAT = RAMAT/1024
        RAMATTT = f'RAM ATUAL:{RAMAT:.2f} MB\n'
        CPU_USAGE = f'CPU USADA:{psutil.cpu_percent()}%\n'

        self.finfosis = [MAQUINA,NOMESISTEMA,VERSAOS,ARQUITETURAPC,PROCESSADOR,RAMATTT,CPU_USAGE]
        self.text1.delete(1.0, END)
        #cria
        for i in self.finfosis:
            self.text1.config(state=NORMAL)
            self.text1.insert(END, i)
        self.text1.config(state=DISABLED)
        self.root1.after(10000,self.func_apaga)

    def func_travarbt(self,status):
        if status == 1:
            def auxiliartrava():
                self.text.insert(END,'Tudo Pronto\nMemoria Ram otimizada\ncache limpo')
                self.barprogress.stop()
                self.Limpezasimples.config(state=NORMAL)
            self.root1.after(180000, auxiliartrava)
            self.barprogress.start(1800)
            self.Limpezasimples.config(state=DISABLED)
        if status == 2:
            def auxiliartrava():
                self.text.insert(END, 'Tudo Pronto\nTodos Processos foram encerrados\ntudo limpo.')
                self.barprogress.stop()
                self.Limpezacompleta.config(state=NORMAL)
            self.root1.after(180000, auxiliartrava)
            self.barprogress.start(1800)
            self.Limpezacompleta.config(state=DISABLED)

    def func_limpezasimples(self):
        '''
        adiciona os comandos para limpeza simples
        :return: None
        '''
        self.func_travarbt(1)#trava o botao
        subprocess.Popen(f'{os.getcwd()}\\oscomands\\s.bat')
        subprocess.Popen(f'{os.getcwd()}\\oscomands\\s1.bat')

    def func_limpezacompleta(self):
        self.func_travarbt(2)
        for processos in psutil.pids():
            info_processo = psutil.Process(processos)  # cria um objeto do tipo process
            inicio = localtime(info_processo._create_time)  # tempo é data de execuçãoo do programa
            if processos == os.getpid():
                pass
            else:
                self.text.delete(1.0, END)
                subprocess.Popen(f'taskkill /pid {processos} ',shell=True)
                x = lambda x=self.text.insert(END, f'''Processo:\n
nome:{info_processo.name()}\n
id:{info_processo.pid}\n
iniciou:{inicio[3]}:{inicio[4]}:{inicio[5]}\n
data:{inicio[2]}/{inicio[1]}/{inicio[0]}\n
esse processo acaba de ser encerrado. '''): x
                self.root1.after(1000,x)
                sleep(1)
                self.text.update()

    def func_limpezarapida(self):
        def auxiliar():
            self.barprogress.stop()
            self.text.insert(END, 'CACHE LIMPO')
        self.barprogress.start(100)
        self.root1.after(10000,auxiliar)
        subprocess.Popen(f'{os.getcwd()}\\oscomands\\s1.bat')

    def func_Login(self):
        '''
        quando o usuario clicar em entrar o prograa chama essa funçao
        :return: None
        '''
        self.func_apagarWID1() # chama a funçao para apagar os widgets
        self.labelmsg['text'] = self.list_name_objects[0]
        self.buttonUni['text'] = 'Entrar'
        self.labelmsg['fg'] = azul
        self.criar_painel() #chama para criar o painel de novo
        self.buttonUni['command'] = partial(self.func_logica_De_cadastro_e_login, 1) #
        print('entrar')#debug

    def func_cadastrar(self):
        '''
        Quando o usuario clicar em Cadastrar o programa chama essa funcao
        :return: None
        '''
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.buttonUni['command'] = partial(self.func_logica_De_cadastro_e_login, 2) ##
        self.labelmsg['text'] = self.list_name_objects[1]
        self.buttonUni['text'] = 'Cadastrar'; self.labelmsg['fg'] = vermelho
        print('cadastrar')#debug

    def func_sair(self):
        '''
        encerra o processo do programa é fecha ele
        :return: None
        '''
        if 'win' in sys.platform:
            subprocess.Popen(f'taskkill /pid {os.getpid()}')
        self.root1.destroy()
        self.root1.quit()

    def func_apagarWID1(self):
        '''
        apaga esse widgets
        :return: None
        '''
        self.label1.grid_forget()  # apagar
        self.entry1.grid_forget()
        self.label2.grid_forget()
        self.entry2.grid_forget()

    def func_apagarWID2(self):
        self.labelmsg.pack_forget()
        self.buttonUni.grid_forget()

    def func_apaga(self):
        '''
        apaga os dados dentro do text1
        '''
        self.text1.config(state=NORMAL)
        self.text1.delete(1.0, END)
        self.func_info_do_sistema()

    def func_limplog(self,null):
        '''
        Faz parte do botao limpar log
        :param null: para á funçao bind não reclamar
        :return: None
        '''
        self.text.delete('1.0',END)

    def func_ajuda(self):
        '''
        Exibe ajuda para o usuario quando ele pedir
        :return: None
        '''
        tkinter.messagebox.showinfo('Ajuda',AJUDA)
