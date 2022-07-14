from classes import main_class
import tkinter


if __name__ == "__main__":
    principal = tkinter.Tk()
    principal.geometry("500x300+430+250")
    principal.title("Calculadora Grafica de Bhaskara")
    principal.resizable(False,False)
    main_class.Bhaskara(principal)
    principal.mainloop()