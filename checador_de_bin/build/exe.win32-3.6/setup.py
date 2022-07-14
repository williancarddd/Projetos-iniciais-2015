from  cx_Freeze import setup,Executable
import os,sys,glob

os.environ['TCL_LIBRARY'] = 'D:\\Python36\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] ='D:\\Python36\\tcl\\tk8.6'

base = None
if sys.platform == "win32":
    base = "Win32GUI"

#pega arquivos
arquivos = []
for arq in glob.glob('*'):
    if '__pycache__' in arq:
        pass
    else:
        arquivos.append(f'{os.getcwd()}\\{arq}')
arquivos.append('D:\\Python36\\DLLs\\tk86t.dll')
arquivos.append('D:\\Python36\\DLLs\\tcl86t.dll')

buildOptions = dict(
      packages = [],

      includes = ['tkinter','requests','json','_thread','tkinter.messagebox','queue','urllib3'],

      include_files = arquivos
)

setup(name='Checker Bin',
      version='1.0',
      description='CARDER 1.0',
      options = dict(build_exe = buildOptions),
      executables=[Executable('main.py',base=base,icon='D:\\checador_De_bin\\imagens\\cartao.ico')]
      )

