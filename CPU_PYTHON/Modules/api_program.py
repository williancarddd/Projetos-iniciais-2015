import platform
import psutil
import datetime


class ApiProgram(object):
    def __init__(self):
        #psutil
        self.numero_de_nucleos_processador = psutil.cpu_count()
        self.cpus_utilizaveis = len(psutil.Process().cpu_affinity())
        self.incio_uso_pc = datetime.datetime.fromtimestamp(psutil.boot_time()).time()
        self.particoes_pc = [particoes[0] for particoes in psutil.disk_partitions()]
        #plataforma
        self.arquitetura_pc = platform.architecture()[0]
        self.tipo_de_maquina = platform.machine()
        self.sistemaOP = platform.platform()
        self.nome_usuario = platform.node()

    def percentual_uso_processador(self):
        return psutil.cpu_percent(0.1)

    def cpu_freq(self):
        return psutil.cpu_freq()

    def salvarDados(self):
        par = ''
        import os
        for dat in self.particoes_pc:
            par += f'{dat}\n'
        string = f"""\
NUMEROS DE NUCLEOS:{self.numero_de_nucleos_processador}
CPUS UTILIZAVEIS:{self.cpus_utilizaveis}
INICIO DO COMPUTAOR:{self.incio_uso_pc}
#######################################
PARTIÇÕES:{par}
#######################################
TIPO:{self.arquitetura_pc}            
TIPO DE MAQUINA:{self.tipo_de_maquina}
SISTENA OPERACIONAL:{self.sistemaOP}  
NOME DO USUARIO:{self.nome_usuario}   """
        with open(f'C:\\Users\\{os.environ["USERNAME"]}\Desktop\DADOS_PC.txt','w') as arq:
            arq.write(string)
