import os,glob

for nome, subdiretorio , arquivo in os.walk('.'):
    print(nome)
    for arquivos in arquivo:
        if '.bmp' in arquivos:
            print(f'arquivo:{arquivos} modificado')
            os.rename(f'{os.getcwd()}\\{nome}\\{arquivos}', f'{os.getcwd()}\\{nome}\\{arquivos}.gif')
