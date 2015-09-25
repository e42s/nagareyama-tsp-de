import random as rd
import numpy as np
import convert as cv

def createind(inds , len_dat):
    tmp = [(rd.sample(range(len_dat) , len_dat)) for col in range(inds)]
    tmp_order = [0 for k in range(inds * len_dat)]

    individual_path = (np.array(tmp).reshape(inds , len_dat))
    individual_order = (np.array(tmp_order).reshape(inds , len_dat))

    # Convert from Path to Order
    individual_order = cv.convertPTO(inds , len_dat , individual_path , individual_order)

    return individual_path , individual_order
