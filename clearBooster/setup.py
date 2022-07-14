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
arquivos.append('D:\Python36\DLLs\tk86t.dll')
arquivos.append('D:\Python36\DLLs\tcl86t.dll')

buildOptions = dict(
      packages = ['os',
                  'sys',
                  'tkinter.ttk',
                  'tkinter.messagebox',
                  'psutil',
                  'subprocess',
                  'ctypes',
                  'time',
                  'functools',
                  'platform'],

      includes = ['tkinter','pymysql'],

      include_files = arquivos
)

setup(name='ClearBooster',
      version='1.0',
      description='O melhor otimizador de sistemas da atualidade, simples,rapido é confiavel.',
      options = dict(build_exe = buildOptions),
      executables=[Executable('main.py',base=base,icon='D:\\clearBooster\imagens\icobooster.ico')]
      )

