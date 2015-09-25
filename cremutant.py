import numpy as np

def mutant(x , S):
    x_1 = np.array(x[0])
    x_2 = np.array(x[1])
    x_3 = np.array(x[2])
    S_minus = []

    minus = x_2 - x_3

    for i in (S * minus):
        # check int or float
        if isinstance(i , int):
            S_minus.append(int(i))
        else:
            S_minus.append(int(round(i)))

    mutant_order = x_1 + S_minus

    return mutant_order
