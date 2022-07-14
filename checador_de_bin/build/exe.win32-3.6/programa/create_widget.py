from programa.bin_checker import *
from programa.variaveis import *
from programa.menu_bt_direito import *
from conect_api import program_logical

class Create_widget(object):
    """
    cria os widget
    """
    def  __init__(self, *master): # recebe varios frames
        # limit carcter
        self.stringvar = tk.StringVar() # class string var
        self.stringvar.trace('w', self.func_limite_caracter)

        #criar botao entrada é texo
        self.entrada1 = tk.Entry(master[0], bg=variaveis.COR3, width=55, font=variaveis.FONTE1,
                             textvariable=self.stringvar)
        self.text1    = tk.Text(master[2], width=68, height=14, font=(variaveis.FONTE1), fg=variaveis.COR4,
                             bg=variaveis.COR3)
        self.botao1   = tk.Button(master[1],text='CHECKER',font=variaveis.FONTE1,bg=variaveis.COR4,
                             activebackground=variaveis.COR3, command=self.func_consulta)

        #empacotar
        self.entrada1.pack()
        self.botao1.pack()
        self.text1.pack(side=LEFT)

        #configurar menu quando clicar com o botao direito sobre a entrada1 é text1
        self.menu_copy_paste = Class_menu() # FAZ PARTE DO MENU BT DIREITO
        self.menu_copy_paste.make_menu(master[0],variaveis.COR3)
        self.entrada1.bind_class('Entry',"<Button-3><ButtonRelease-3>",self.menu_copy_paste.show_menu)
        self.text1.bind_class('Text',"<Button-3><ButtonRelease-3>", self.menu_copy_paste.show_menu )

        #nome na caixa de entrada
        FistClick(self.entrada1, 'Insert a Bin...') # adicona 'Insira á bin'  FAZ PARTE DO MENU BT DIREITO

        #focus force foca o widget
        self.entrada1.focus_force()
        self.text1.focus_force()

        #chamar funçao
        self.func_consulta()

    def func_limite_caracter(self,*arsg):
        ''''
        limite de caracters na caxa de entrada
        '''
        value = self.entrada1.get()
        if len(value) > 50: self.stringvar.set(value[:2])

    def func_consulta(self):
        self.consultar  = program_logical.Requisicao(self.entrada1, self.text1, self.botao1) # recebe widgets

