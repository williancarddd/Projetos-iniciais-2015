import tkinter
from Constants import variables
from Modules import api_program
import _thread

class MainCreator(object):
    def __init__(self, master:object) -> 'Construtor do objeto':
        #CANVAS E TELAS
        self.master = master
        self.master['background'] = variables.preto_claro
        self.canvas1 = tkinter.Canvas(self.master, bg=variables.preto_claro, width=variables.width // 2, highlightthickness=0)
        self.canvas2 = tkinter.Canvas(self.master, bg=variables.preto_claro, width=variables.width // 2, highlightthickness=0)
        self.canvas1.pack(side=tkinter.LEFT)
        self.canvas2.pack(side=tkinter.LEFT)

        #dados pc
        self.dados_pc = api_program.ApiProgram()

        #menu de opçoes
        self.barraMenu = tkinter.Menu(self.master)                       # barra principal
        self.Menu_config = tkinter.Menu(self.barraMenu, tearoff=0)       # menu dentro do menu
        self.barraMenu.add_cascade(label='Menu', menu=self.Menu_config)  # opçao de menu
        self.Menu_config.add_command(label='Salvar dados', command=self.salvarDados)
        self.Menu_config.add_command(label='Sair', command=self.FecharPrograma)
        self.master.config(menu=self.barraMenu)                          # configura menu

        self.canvas1.create_text(variables.width/4,10, text='CPU', fill=variables.verde_forte, font=variables.fonte1)
        self.canvas2.create_text(variables.width/4,12, text='SISTEMA', fill=variables.verde_forte, font=variables.fonte1)
        self.canvas1.create_text(variables.width/5, 255, text=f'USUARIO:{self.dados_pc.nome_usuario}', fill=variables.verde_forte)

        self.texto1 = tkinter.Text(self.canvas1,
                                   bg=variables.preto_claro,
                                   relief=tkinter.SOLID,
                                   fg=variables.verde_forte)
        self.texto1.place(x=variables.width/23, y=30, height=210,width=200)

        self.texto2 = tkinter.Text(self.canvas2,
                                   bg=variables.preto_claro,
                                   relief=tkinter.SOLID,
                                   fg=variables.verde_forte)
        self.texto2.place(x=variables.width / 80, y=30, height=210, width=158)

        self.scrollbar_Texto1 = tkinter.Scrollbar(self.master, command=self.texto1.yview)
        self.scrollbar_Texto1.place(x=180, y=45)
        self.texto1['yscrollcommand'] = self.scrollbar_Texto1.set
        self.scrollbar_Texto2 = tkinter.Scrollbar(self.master, command=self.texto2.yview)
        self.scrollbar_Texto2.place(x=366, y=40)
        self.texto2['yscrollcommand'] = self.scrollbar_Texto2.set


        _thread.start_new_thread(self.dados_atualizacao, ())
        self.particao_formatada = ''
        for ff in self.dados_pc.particoes_pc:
            self.particao_formatada += f'\n--{ff}'

    def dados_atualizacao(self):
        string1 = f"""PARTIÇÕES:{self.particao_formatada}
NUCLEOS:{self.dados_pc.numero_de_nucleos_processador}\n\
----UTILIZAVEIS:{self.dados_pc.cpus_utilizaveis}
[+]BOOT:{self.dados_pc.incio_uso_pc}
[+]PROCESSADOR:{self.dados_pc.percentual_uso_processador()}%
----{self.dados_pc.cpu_freq().current} de {self.dados_pc.cpu_freq().max}"""
        self.texto1.delete(0.0, tkinter.END)
        self.texto1.insert(0.0, string1)

        string2 = f"""
{self.dados_pc.sistemaOP}
TIPO:{self.dados_pc.arquitetura_pc}
MAQUINA:{self.dados_pc.tipo_de_maquina}

"""

        self.texto2.delete(0.0, tkinter.END)
        self.texto2.insert(0.0, string2)
        self.texto1.after(1000,self.dados_atualizacao)


    def salvarDados(self):
        self.dados_pc.salvarDados()

    def FecharPrograma(self):
        self.master.destroy()