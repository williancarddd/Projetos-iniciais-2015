import platform
import psutil
#GEOMETRIA DO PROGRAMA (TAMANHO DA TELA)
GEOMETRY = f'600x300+{600//2}+{600//2}' #f'350x350+{350//2}+{350//2}'

#TITULO DO PROGRAMA
TITLE = 'Clear Booster'

#Fonte
FONTElabe = 'Helvetica'
TamanhoFG = 13
azul = '#2920FF'
vermelho = 'Red'
branco= 'White'
verde_florescente = "#39FF14"
preto_meioclaro = '#090909'
azul_modificado = '#130FFF'

#espaçamento etre os widgets
Pdx = 5

#status de ajuda dos botoes
LCOMPLETA = '\n\nA Limpeza Completa Ela é Mais Profunda é Mais Intensa No Seu Sistema,\n' \
            'é Por isso ela Demora Mais Para Ser Concluida.' \
            '\n\nOBS:Oque Estiver Sendo Executado No Momento Ira Ser Encerrado.'

LSIMPLES = '\n\nA Limpeza Simples Ela Só irar Limpar o Cache é A Memoria Ram'
LRAPIDA = '\nA Limpeza Rapida Só Irar Limpar O Cacher'
AJUDA = 'Ola bem vindo ao nosso aplicativo de otimização de sistema.\n' \
        'possiveis ajuda:\n\n' \
        'Como usar o programa? só tem como usa-lo cadastrando-se nele,sabemos que é chato mas e para termos controle\n' \
        'de quantas pessoas estão usando nosso aplicativo.\n\n' \
        'Como cadastrar? Você se cadastra clicando em Menu ->cadastrar.\nespecificaçoes:\nO usario tem que ser valido é maior que 4 caracteres\n' \
        'a senha não pode ser menor que 5 caracteres.\n\n' \
        'AVISO: O botão é bloqueia acada 4 cliques, espere 5 segundos para destravas.\n\n' # MENU DE AJUDA/

#INFORMAÇOES DO SISTEMA
MAQUINA = f'MAQUINA:{platform.platform()}\n'
NOMESISTEMA = f'SISTEMA OPERACIONAL:{platform.system()}\n'
VERSAOS = f'VERSÃO DO SISTEMA:{platform.version()}\n'
ARQUITETURAPC = f'ARQUITETURA:{platform.machine()}\n'
PROCESSADOR = f'PROCESSADOR:{platform.processor()}\n\n'


#variaveis de query sql do programa (dbs)
query_inserirDD = 'INSERT INTO Bc_ClearBooster.Bc_ClearBooster VALUES("{}","{}")'
queryconsu = 'SELECT usuario,senhauser FROM bc_clearbooster.bc_clearbooster WHERE usuario = "{}" and senhauser = "{}" '
query_consultarusuario = 'SELECT usuario FROM  bc_clearbooster.bc_clearbooster WHERE usuario = "{}" '