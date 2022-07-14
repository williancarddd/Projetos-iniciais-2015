import requests
from variaveis import variaveis
from DB_dataBase  import Db_class
import json.decoder

def api_requests(widget, cep):
    try:
        instancia_do_banco = Db_class.DataBase()
        resultado = instancia_do_banco.ConsultarDados(cep=cep)
        if resultado:
            print(1)
            for indice, passador in enumerate(resultado[0]):
              widget.insert(1.0,f'{instancia_do_banco.indice_db[indice]}:{passador}\n')
        else:
            requisicao = requests.get(url=variaveis.API+str(cep))
            json_consulta = requisicao.json()
            print(json_consulta)
            for passador in json_consulta:
                if passador == 'cidade_info':
                    continue
                else:
                    widget.insert(1.0, f'{passador}: {json_consulta[passador]}\n')
            else:
                if 'complemento' not in  json_consulta.keys():
                    json_consulta['complemento'] = 'Sem complemento'
            print(json_consulta)
            instancia_do_banco.EntradaDeDados(**json_consulta)


    except json.decoder.JSONDecodeError:
        widget.insert(1.0,'CEP INVALIDO')
    except Exception as error:
        print(error, 'api')
