from math import sqrt
import tkinter
import matplotlib.pyplot as plt
import numpy as np



class Bhaskara(object):
    def __init__(self, root):
        self.root =  root
        self.__status = ["Insira A ,B e C sem o X","Insira apenas Numeros"]


        self.A = tkinter.Label(self.root, text="A =", font="arial 16")
        self.A.place(x=50, y=30)

        self.B = tkinter.Label(self.root, text="B =",font="arial 16")
        self.B.place(x=130, y=30)

        self.C = tkinter.Label(self.root, text="C =",font="arial 16")
        self.C.place(x=210, y=30)

        self.entrada_A = tkinter.Entry(self.root, bg="red")
        self.entrada_A.place(x=99, y=38, width=25)

        self.entrada_B = tkinter.Entry(self.root, bg="red")
        self.entrada_B.place(x=180, y=38, width=25)

        self.entrada_C =  tkinter.Entry(self.root, bg="red")
        self.entrada_C.place(x=260, y=38, width=25)

        self.botao_resposta = tkinter.Button(self.root, text="Calcular", bg="red", font="arial 16", command= self.__calcular_bhaskara)
        self.botao_resposta.place(x=50, y=90)

        self.canvas_grafico = tkinter.Canvas(self.root, bg='black')
        self.canvas_grafico.place(x=290, y=5, width=220)

        self.label_status =  tkinter.Label(self.root, text=self.__status[0], font="arial")
        self.label_status.place(x=10, y=200)



    def __calcular_bhaskara(self):
        try:
            self.__A, self.__B, self.__C = int(self.entrada_A.get()), int(self.entrada_B.get()), int(self.entrada_C.get())
            self.delta = (self.__B**2) - (4* self.__A * self.__C)
            self.bhaskara_resultado_mais = (-self.__B + sqrt(self.delta)) / 2 * self.__A
            self.bhaskara_resultado_menos = (-self.__B - sqrt(self.delta)) / 2 * self.__A
            self.vertice_x = -(self.__B)/(2*self.__A)
            self.vertice_y = - (self.delta) /  (4*self.__A)
            self.desenhar_eixo()


            print(self.bhaskara_resultado_mais)
            print(self.bhaskara_resultado_menos)

        except ValueError as error:
            print(f"debug {self.__status[1]}", error)
            self.label_status['text'] = self.__status[1]

    def desenhar_eixo(self):
      eixo_x = []
      eixo_y = []
      zero =  []

      variacao = abs(self.bhaskara_resultado_mais - self.bhaskara_resultado_menos)
      if variacao < 3: variacao = 3

      for x in np.arange(self.bhaskara_resultado_mais - variacao, self.bhaskara_resultado_menos + variacao,variacao/100):
          y = self.__A * (x**2) + self.__B*(x)+self.__C
          eixo_x.append(x)
          eixo_y.append(y)
          zero.append(0.0)
      plt.plot(eixo_x, eixo_y, color='blue')
      plt.plot(eixo_x, zero, color ="black")
      plt.show()

