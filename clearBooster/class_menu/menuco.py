from tkinter import *
class Class_menu(object):
    '''
    essa classe cria o menu de copiar, colar é corta
    ela cria o menu aonde o usuario clicou.
    obs: onde foi definido que tenha o menu

    '''

    def make_menu(self,w):
        '''
        :param w: instancia de tkinter
        :return :None

        essa funçao cria o menu
        '''
        self.the_menu = Menu(w,tearoff=0)
        self.the_menu.add_command(label="Cortar")
        self.the_menu.add_command(label="Copiar")
        self.the_menu.add_command(label="Colar")

    def show_menu(self,e):
        '''

        :param e: pega o retorno de bind_class
        :return: None
        cria as funcionalidades.
        '''
        w = e.widget
        self.the_menu.entryconfigure("Cortar",command=lambda: w.event_generate("<<Cut>>"))
        self.the_menu.entryconfigure("Copiar",command=lambda: w.event_generate("<<Copy>>"))
        self.the_menu.entryconfigure("Colar",command=lambda: w.event_generate("<<Paste>>"))
        self.the_menu.tk.call("tk_popup", self.the_menu, e.x_root, e.y_root)

#t = Tk()
#a = menu()
#a.make_menu(t)

#e = Entry();e.pack()
#e.bind_class('Entry',"<Button-3><ButtonRelease-3>",a.show_menu)
#t.mainloop()