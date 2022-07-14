import sqlite3

class Banco_De_Dados(object):
    def __init__(self):
        self.conexao = sqlite3.connect('Banco_registros.db') # conecta no banco
        self.cursor = self.conexao.cursor() # editor do banco
        self.cria_tabela()

    def cria_tabela(self):
        sql1 = 'CREATE TABLE IF NOT EXISTS cadastrados(nome text,senha text,email text)'
        self.cursor.execute(sql1)
        # cria tabela se nao existir uma com nome cadastrados
    def criar_perfil(self ,nome ,senha ,email):
        '''
        Essa  funcao registra dados no banco////////////
        '''
        sql2 = 'INSERT INTO  cadastrados VALUES(?, ?, ?)'
        self.cursor.execute(sql2,(nome,senha,email))
        self.conexao.commit()

    def verifica_se_existe_usuario(self,usuario_get):
        sql3 = "SELECT * FROM cadastrados "#seleciona a coluna de usuario
        consulta1 = self.cursor.execute(sql3)
        for passeador in consulta1:
           if passeador[0]  == usuario_get:
               return  False

    def verifica_email(self, email_get):
        sql4 = 'SELECT * FROM cadastrados'
        consulta2 = self.cursor.execute(sql4)
        for passeador2 in consulta2:
            if passeador2[2] == email_get:
                return False

    def verifica_senha(self,senha_get):
        sql4 = "SELECT * FROM cadastrados"
        consulta3 = self.cursor.execute(sql4)
        for passeador3 in consulta3:
            if passeador3 == senha_get:
                return  False
