import random as rd
import numpy as np

def createind(inds , len_dat):
    tmp = [(rd.sample(range(len_dat) , len_dat)) for col in range(inds)]
    tmp_order = [0 for k in range(inds * len_dat)]

    individual_path = (np.array(tmp).reshape(inds , len_dat))
    individual_order = (np.array(tmp_order).reshape(inds , len_dat))

    # Convert from Path to Order
    for i in range(inds):
        city = [n for n in range(len_dat)]
        for j in range(len(city)):
            individual_order[i , j] = city.index(individual_path[i , j])
            city.pop(city.index(individual_path[i , j]))

    return individual_path[:] , individual_order[:]
