import numpy as np
import random as rd

def select(inds , individual_path , individual_order):

    select_random = [rd.sample(range(inds) , 3) for n in range(3)]

    path = [individual_path[select_random[n]] for n in range(len(select_random))]
    order = [individual_order[select_random[n]] for n in range(len(select_random))]

    return path , order
