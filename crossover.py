import random as rd

def crossover(inds_1 , inds_2):

    # 一様交叉
    # マスク作る
    mask = [rd.randint(0 , 1) for n in range(len(inds_1))]
    result = []

    # 0 or 1
    for i in range(len(mask)):
        if mask[i] == 0:
            result.append(inds_1[i])
        elif mask[i] == 1:
            result.append(inds_2[i])

    return result
