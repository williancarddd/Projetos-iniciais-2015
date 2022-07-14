from ClearBooster  import *
import sys,os

#def is_admin():
 #   try:
  #      return ctypes.windll.shell32.IsUserAnAdmin()
   # except:
    #   return False

if __name__ == '__main__':
 #   if is_admin():
        instance = Tk()
        instance.title(TITLE)
        instance.geometry(GEOMETRY)
        instance.resizable(False, False)
        instance.wm_iconbitmap(f'imagens{os.sep}icobooster.ico')  # icone na pasta imagens
        Main(instance)
        instance.mainloop()
  #  else:
         #Re-run the program with admin rights
   #     ctypes.windll.shell32.ShellExecuteW(None, "runas",sys.executable, "", None, 1)
