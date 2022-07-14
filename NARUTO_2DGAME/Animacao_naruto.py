import tkinter, time
from PIL import Image, ImageTk
from contents import variables

WIDTH, HEIGHT  = 640, 360
class Naruto_movimetetion(object):
    def __init__(self, master):
        self.screen = master                                  # tela principal
        self.spriteshet_correndo = []                         # imagens sprite
        self.spriteshet_correndo_esquerda = []
        self.spriteshet_parado = []
        self.spriteshet_rasengshuriken = []
        self.image_Reference = []                             # referencia de imagem caso de bug

        self.correndo = self.parado_I = self.correndo1 = 0    # total de imagem dele no jogo
        self.rasegan_shu = self.lancamento = 0
        self.velocidade = variables.VELOCIDADE                #velocidade personagem
        self.xy_naruto = variables.POSICAO_INICIAL_DO_NARUTO  # posicao inicial do naruto
        self.barra_de_chackra =  variables.CHACKRA_PERSONAGEM #chackra
        self.barra_de_vida    =  variables.VIDA_PERSONAGEM    #vida
        self.rosa_dos_ventos = 0                              # recebe só 1,2,3 para saber á direçaão


        self.canvas = tkinter.Canvas(self.screen, bg='green', width=WIDTH, height=HEIGHT) # canvas principal
        self.canvas.pack()

        Exibir_cenario(self.canvas, self.image_Reference) #cenario

        self.canvas.create_rectangle(self.barra_de_chackra, fill='Blue', tag='barra_chackra') # barra de chackra
        self.canvas.create_rectangle(self.barra_de_vida, fill='red', tag='barra_vida') # barra de vida


        #carregamento de imagens
        for carregar in range(136, 140+1): # carrega á imagem dele correndo é armazena em uma lista
            self.spriteshet_correndo.append(ImageTk.PhotoImage(Image.open(f'NARUTO\CORENDO\\naruto{carregar}.bmp.gif')))

        for carregar in range(136, 140+1):
            self.spriteshet_correndo_esquerda.append(ImageTk.PhotoImage(Image.open(f'NARUTO\CORENDO\\narutoE{carregar}.bmp.gif')))

        for carregar in range(126, 128+1):
            self.spriteshet_parado.append(ImageTk.PhotoImage(Image.open(f'NARUTO/PARADO/naruto{carregar}.bmp.gif')))

        for carregar in range(432, 435+1):
            self.spriteshet_rasengshuriken.append(ImageTk.PhotoImage(Image.open(f'NARUTO/RASENGASHURIKEN/NARUTOS{carregar}.bmp.gif')))

        #eventos
        self.screen.bind('<Right>', self.func_direita) # vai para á direita
        self.screen.bind('<Left>', self.func_esquerda) # vai para á esquerda
        self.screen.bind('<space>', self.rasegan_shuriken) #tecla de espaco
        self.reconstroi_barra_de_chackra()
        self.carregar_chackra()
        self.configura_chackra()
        self.func_personagem_parado()



    def animacao_poder(self):
        self.canvas.delete('PODER_1')

        if self.rasegan_shu == 4:
            self.rasegan_shu = 0

        self.canvas.create_image(self.x_poder , self.y_poder-23,image=self.spriteshet_rasengshuriken[self.rasegan_shu], tag='PODER_1')
        self.rasegan_shu += 1
        self.id_1 = self.canvas.after(100, self.animacao_poder)

    def rasegan_shuriken(self, none=None):
        if self.x_poder >= WIDTH-90:
            self.canvas.after_cancel(self.id_1)
            self.canvas.delete('PODER_1')
        else:
            self.x_poder += 30
            self.animacao_poder()

    def carregar_chackra(self):
        if self.barra_de_chackra[2] >= 190:
            print('debug: chackra full')
        else:
            if self.barra_de_chackra[2] <= 170:
                print('debug: mais 20 de mana')
                self.barra_de_chackra[2] += 10

        self.canvas.after(1900, self.carregar_chackra) #1

    def reconstroi_barra_de_chackra(self):
        self.x_poder = self.xy_naruto[0]
        self.y_poder = self.xy_naruto[1]

        self.canvas.delete('barra_chackra')  # deleta á barra
        self.canvas.create_rectangle(self.barra_de_chackra, fill='Blue', tag='barra_chackra')  # reconstroi á barra
        self.screen.after(1, self.reconstroi_barra_de_chackra) # 2

    def configura_chackra(self):
        if self.barra_de_chackra[2] <= 0:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2 - 2, text='SEU CHACKRA ACABOU', font=('Helvetica', 20),fill='#DEDA25', tag='INFO1')
            self.velocidade = 5.0 # se á barra de chackra for menor que 0 irar reduzir á velocidade

        else:
            self.velocidade = 9.0
            self.canvas.delete('INFO1')

        self.canvas.after(1, self.configura_chackra) #3

    def func_personagem_parado(self):
        self.canvas.delete('PARADO_1', 'NARUTO_1', 'NARUTO_2')
        if self.parado_I == 3:
            self.parado_I = 0

        self.canvas.create_image(self.xy_naruto, image=self.spriteshet_parado[self.parado_I], tag='PARADO_1')
        self.parado_I += 1
        self.canvas.after(299, self.func_personagem_parado)

    def func_direita(self, Event= None):
        self.canvas.delete('NARUTO_1', 'NARUTO_2', 'PARADO_1')
        if self.correndo == 5:
            print('debug: chegou á 5 imagens'); self.correndo = 0
            self.config_consumo_chackra('Movimentacao') # se for 5 imagens ele chama  essa imagen

        if self.xy_naruto[0] >= WIDTH-19: # se bater na parede
            self.velocidade = 0
            print('debug: exedeu o limite da direita')

        self.canvas.create_image(self.xy_naruto, image=self.spriteshet_correndo[self.correndo], tag='NARUTO_1')
        self.xy_naruto[0] += self.velocidade # velocidade naruto
        self.correndo += 1 # frente
        print('debug: correndo direita')

    def func_esquerda(self, event=None):
        self.canvas.delete('NARUTO_1', 'NARUTO_2', 'PARADO_1') # para nao bugas as imagens
        if self.correndo1 >= 5:
            self.correndo1 = 0
            print('debug: chegou á 5 imagens indo para direita')
            self.config_consumo_chackra('Movimentacao')

        if self.xy_naruto[0] <= 10 :
            self.velocidade = 0.0
            print('debug: exedeu o limite da esquerda')

        self.canvas.create_image(self.xy_naruto ,image= self.spriteshet_correndo_esquerda[self.correndo1], tag='NARUTO_2')
        self.xy_naruto[0] -= self.velocidade #trás
        self.correndo1 += 1

        print('debug: correndo esquerda')

    def config_consumo_chackra(self, event=None):
        print(f'debug: xy: {self.xy_naruto}')
        if event == 'Movimentacao':
            if self.barra_de_chackra[2] >=  0:  self.barra_de_chackra[2] -= 5#<<<<<< menos isso de chackra
            else: pass # se barra de chackra for maior que 0

class Exibir_cenario(object):
    def __init__(self,  canvas , reference):
        self.__canvas =  canvas
        self.__image_Reference = reference
        self.__image_Reference.append(ImageTk.PhotoImage(Image.open('NARUTO\CENARIOS\Campo_de_Entrenamiento.png')))
        self.__canvas.create_image(WIDTH // 2, HEIGHT // 2, image=self.__image_Reference[0])


if __name__ == '__main__':
    janela = tkinter.Tk()
    Naruto_movimetetion(janela)
    janela.geometry(f'{WIDTH}x{HEIGHT}+500+200')
    janela.title(f"{variables.TITULO}")
    janela.resizable(False,  False)
    janela.mainloop()