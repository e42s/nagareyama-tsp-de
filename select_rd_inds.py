import numpy as np
import random as rd

def select(inds , individual_path , individual_order , j , len_dat):

    select_random = rd.sample(range(inds) , 3)

    # 親個体と被っていないか
    while j in select_random:
        select_random = rd.sample(range(inds) , 3)

    tmp_path = [individual_path[n] for n in select_random]
    tmp_order = [individual_order[n] for n in select_random]

    path = np.array(tmp_path).reshape(3 , len_dat)
    order = np.array(tmp_order).reshape(3, len_dat)

    return path , order
