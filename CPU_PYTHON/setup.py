from  cx_Freeze import setup,Executable
import os,sys,glob

os.environ['TCL_LIBRARY'] = 'E:\Python36\PythonATT\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] ='E:\Python36\PythonATT\\tcl\\tk8.6'

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
arquivos.append('E:\Python36\PythonATT\DLLs\\tk86t.dll')
arquivos.append('E:\Python36\PythonATT\DLLs\\tcl86t.dll')

buildOptions = dict(
      packages = [],

      includes = ['tkinter','psutil','os','datetime','platform','_thread'],

      include_files = arquivos
)

setup(name='CPU Python',
      version='0.01',
      description='CPU 0.01',
      options = dict(build_exe = buildOptions),
      executables=[Executable('main.py',base=base,icon='Image/processor_icone_color.ico')]
      )

