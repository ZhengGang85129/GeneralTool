import os,sys 
import math
import time
import tracemalloc
import os ,sys
CURRENT_WORKDIR = os.getcwd()
sys.path.append(CURRENT_WORKDIR)
from GeneralTool.Colors import Colors
import GeneralTool.ShellStyles

def convert_size(size_bytes) -> str:
    if size_bytes == 0:
        return "0B"
    size_name = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "{} {}".format(s, size_name[i])



def MemoryMeasure(Function_Name="", verbose = False)->None:
    def Inner(func):
        def MemoryMeasure_Wrapper(*args, **kwargs):
            tracemalloc.start()
            func(*args, **kwargs)
            current, peak = tracemalloc.get_traced_memory()
            if verbose:
                print(ShellStyles.HighlightStyle() + '---------------------------------------------------------------' + ShellStyles.NormalStyle())
                print('current memory size:' + ShellStyles.ResultStyle() + f' {convert_size(current)}' +  ShellStyles.NormalStyle() + ', peak memory size:'+ ShellStyles.ResultStyle()  +f' {convert_size(peak)} '+ ShellStyles.NormalStyle()  +'after Function '+ ShellStyles.CyanStyle() +f'`{Function_Name}`'+ ShellStyles.NormalStyle())
                if Function_Name == "":
                    print(ShellStyles.WarningLabel() + 'Function name is not specified in MemoryMeasure')
        return MemoryMeasure_Wrapper
    
    return Inner


def TimeMeasure(Function_Name="", verbose = False)->None:
    def Inner(func):
        def TimeMeasure_Wrapper(*args, **kwargs):
            time0 = time.time()
            func(*args, **kwargs)
            if verbose:
                print(f'Run Time for Function '+ ShellStyles.CyanStyle()  +f'`{Function_Name}`'+ ShellStyles.NormalStyle() + ' is :'+ ShellStyles.SuccessStyle() +f'{time.time()-time0:.2f} sec' + ShellStyles.NormalStyle())
                if Function_Name == "":
                    print(ShellStyles.WarningLabel() + 'Function name is not specified in TimeMeasure')
        return TimeMeasure_Wrapper
    return Inner

