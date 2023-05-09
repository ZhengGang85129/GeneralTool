import os,sys 
import math
import time
import tracemalloc
import os ,sys
CURRENT_WORKDIR = os.getcwd()
sys.path.append(CURRENT_WORKDIR)
from GeneralTool.Colors import Colors




def CheckDir(Dir_to_check="",MakeDir=True,quiet=False):
    '''
        Just check whether a folder is existed or not. If it is not, then create a new one.
    '''
                    
    if os.path.isdir(Dir_to_check): return True
    else:
        if not quiet:
            print("\n"+Colors.LIGHT_GREEN+"Warning"+Colors.END+": You don't have directory: "+Colors.YELLOW+Colors.UNDERLINE+ f"{Dir_to_check}"+Colors.END+" under "+Colors.BROWN+Colors.UNDERLINE+f"{CURRENT_WORKDIR}"+Colors.END)
        if MakeDir:
            os.system('mkdir -p {}'.format(os.path.join(CURRENT_WORKDIR,Dir_to_check)))
            if not quiet:
                print(f"\n \033[0;32m Warning \033[0;m: Dir-> \033[0;32m{Dir_to_check}\033[0;m is made now.\n")
        else:pass
        if not quiet:
            print("")
        return False

def CheckFile(File_to_check='',RemoveFile=False,quiet=False):


    '''
    Just check if file is existed or not. Here the function provides a further option
    to let users decide whether this existed file should be deleted or not.
    '''

    if os.path.isfile(File_to_check): 
        if not quiet:
            print('\n \033[0;32m Warning \033[0;m : File->\033[0;33m\033[4m{}\033[0;m exists\n'.format(File_to_check))
        if RemoveFile:
            if not quiet:
                print('\n \033[0;32m Warning \033[0;m : Remove File->\033[0;31m\033[4m{}\033[0;m\n'.format(File_to_check))
            os.system('rm -f {}'.format(File_to_check))
        return True
    else:
        if not quiet:

            print('\n \033[0;32m Warning \033[0;m : File->\033[0;33m\033[4m{}\033[0;m does not exist\n'.format(File_to_check))

        return False

