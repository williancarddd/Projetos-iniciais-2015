import sqlite3


class DataBase(object):
    def __init__(self):
        self.QUERY1 = "CREATE TABLE IF NOT EXISTS  dados_ceppp (cep TEXT,complemento TEXT," \
                 "rua TEXT, bairro TEXT, cidade TEXT,  estado TEXT)"

        self.QUERY2 = "INSERT INTO dados_ceppp  VALUES (?,?,?,?,?,?)"
        self.QUERY3 = "SELECT * FROM dados_ceppp where cep=?"

        self.connection = sqlite3.connect('\Meu_Cep\DB_dataBase\endereçoes.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.QUERY1)
        self.indice_db = ['cep', 'complemento','longradouro', 'bairro', 'cidade' , 'estado']


    def EntradaDeDados(self, **kwargs):
        try:
            self.cursor.execute(self.QUERY2, (kwargs['cep'],kwargs['complemento'], kwargs['logradouro'], kwargs['bairro'], kwargs['cidade'], kwargs['estado']))
            self.connection.commit()
        except Exception as error:
            print(error)


    def ConsultarDados(self, cep):
        self.cursor.execute(self.QUERY3, (cep, ))
        data = self.cursor.fetchall()
        if data: # se for verdadeiro cep esta no banco de dados
            print(data,'DEBUG DBBBBBBBBBB')
            return data
            #tem dados
        else:
            #nao tem
            return False


a = DataBase()
#a.EntradaDeDados('7680802','5507','aroeira','coahb','porto velho','5353','ro')

