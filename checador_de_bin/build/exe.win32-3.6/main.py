from programa.bin_checker import *
from programa import  variaveis

if __name__ == '__main__':
    janel = tk.Tk()
    Main_bin(janel)  # executa o programa programa
    janel.resizable(False,False) #desativa redefinição de tela
    janel.geometry(variaveis.TAMANHO_JANELA) #tamanho da tela
    janel.wm_iconbitmap(f'D:\\checador_de_bin\\imagens\\cartao.ico') #icone de cartao
    janel.title(variaveis.TITULO_PROGRAMA)#titulo
    janel.mainloop() # inicia