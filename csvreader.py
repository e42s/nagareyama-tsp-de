import pandas as pd

def reader():
    dat = pd.read_csv('att48.csv' , header = None)
    len_dat = len(dat)

    return dat[:] , len_dat
