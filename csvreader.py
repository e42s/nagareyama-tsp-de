import pandas as pd

def reader():
    dat = pd.read_csv('nagareyama.csv' , header = None)
    len_dat = len(dat)

    return dat[:] , len_dat
