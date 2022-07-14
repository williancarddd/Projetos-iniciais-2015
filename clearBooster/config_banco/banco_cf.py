import  pymysql
from variaveisproject import *

class CFB(object):
    """
    As querys estao no variaveisproject
    """
    def __init__(self):
        self.conexao = pymysql.connect(host='127.0.0.1',
                                       user='root',
                                       passwd='william15',
                                       db='Bc_ClearBooster',
                                       port=3306
                                       )
        self.cursor = self.conexao.cursor()
       
    def inserir_dados(self,nome,senha):
        resulta_consulta_nome = self.cursor.execute(query_consultarusuario.format(nome))

        if resulta_consulta_nome > 0: # se for maior que zero o usuario ja esta cadastrado
            print('usuario ja cadastrado')#debug
            return False

        else:# ele nao esta cadastrado
            self.cursor.execute(query_inserirDD.format(nome,senha))
            self.conexao.commit()
            return True

    def consultar_dados(self,nome,senha):
        executar_query = self.cursor.execute(queryconsu.format(nome, senha))
        print(self.cursor.fetchall())#debug

        if executar_query == 1:
            return True
        else:
            return False

