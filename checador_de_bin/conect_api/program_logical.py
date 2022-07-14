from requests import get
import _thread,json
from programa.bin_checker import *
'''
api:https://api-center.000webhostapp.com/api/apistore_binchecker.php?bin=5555
'''
API = 'https://api-center.000webhostapp.com/api/apistore_binchecker.php?bin=555'
class Requisicao(object):
    def __init__(self, *widget):
        self.__widge1 = widget[0] # entrda
        self.__widget2 = widget[1] # saida
        self.__widget3 = widget[2] # botao
        #chamar func
        self.func_valida()

    def func_valida(self):
        self.__bin = self.__widge1.get() # ENTRADA DO USUARIO
        if len(self.__bin) < 5: # PARA MEXER COM WIDGETS DE TEXTO TEEM QUE ESTA state:NORMAL

            self.__widget2.config(state=tk.NORMAL)
            self.__widget2.delete(1.0,tk.END)
            self.__widget2.insert(tk.END,'BIN INVALIDA\n')
            self.__widget2.config(state=tk.DISABLED)

        else:
            self.__widget2.config(state=tk.NORMAL)
            try:
                _thread.start_new_thread(self.dados,(self.__bin,))

            except Exception as error:
                print('deu pau',error)

            self.__widget2.config(state=tk.DISABLED)
            self.__widget2.config(state=tk.NORMAL)

    def dados(self,bin):
        try:
            self.__widget2.delete(1.0,tk.END)
            self.resque = get(f'https://api-center.000webhostapp.com/api/apistore_binchecker.php?bin={bin}')
            self.dataform = str(self.resque.text).strip("'<>() ").replace('\'', '\"') # remove '<>()
            self.jsonreque = json.loads(f'{self.dataform}')
            __lista_chaves = ["bin","brand","type","level","bank","country","phone","site","countryCode","status"]
            for up in __lista_chaves:
                self.__widget2.insert(tk.END,f'{up}:{self.jsonreque[up]}\n')

        except Exception as erro:
            print('deu pau na dados',erro)
