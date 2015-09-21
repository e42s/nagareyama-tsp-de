import random as rd
import numpy as np

def crossover(inds_1 , inds_2):

    # 交叉する
    sepapoint = rd.randint(1 , len(inds_1))

    tmp_f_1 = inds_1[: sepapoint].tolist()
    tmp_b_2 = inds_2[sepapoint :].tolist()

    tmp_f_1.extend(tmp_b_2)
    newinds_1 = tmp_f_1

    return newinds_1[:]
