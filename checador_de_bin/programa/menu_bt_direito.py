from tkinter import *

class Class_menu(object):
    '''
    essa classe cria o menu de copiar, colar é corta
    ela cria o menu aonde o usuario clicou.
    obs: onde foi definido que tenha o menu

    '''

    def make_menu(self,w,cor='White'):
        '''
        :param w:frame onde sera criado
        :param cor: especifique uma cor para o widget
        :return :None

        essa funçao cria o menu
        '''
        self.the_menu = Menu(w,tearoff=0,bg=cor)
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
#exemplo de uso
#t = Tk()
#a = class_menu()
#a.make_menu(t)

#e = Entry();e.pack()
#e.bind_class('Entry',"<Button-3><ButtonRelease-3>",a.show_menu)
#t.mainloop()
        
class FistClick(object):
    '''
    essa classe permite que voce insira uma mensagem como background em  um entry
    '''
    def __init__(self,widget,backgroudntext='Insert to text'):
        self.text = backgroudntext
        self.widget = widget
        self.widget.insert(0, self.text)
        self.widget.bind('<FocusIn>', self.__clickon)
        self.widget.bind('<FocusOut>',self.__clickout)

    def __clickon(self,event):
        if self.widget.get() == self.text:
            self.widget.delete(0, "end")  # delete all the text in the entry
            self.widget.insert(0, '')  # Insert blank for user input
            self.widget.config(fg='black')

    def __clickout(self, event):
        if self.widget.get() == self.text:
            self.widget.insert(0, self.text)
            self.widget.config(fg='grey')

