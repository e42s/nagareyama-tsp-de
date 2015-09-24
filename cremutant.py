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

    prototype_mutant = x_1 + S_minus

    mutant_order = []
    for n in prototype_mutant:
        if n >= 0 and n < len(x_1) - 1:
            mutant_order.append(n)
        elif n < 0 or n >= len(x_1):
            mutant_order.append(0)

    return mutant_order
