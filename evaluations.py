import math
import numpy as np

def distance(pos1 , pos2):
    # Demand the oblique side using Pythagorean theorem
    dist = math.sqrt(((pos1[0] - pos2[0]) ** 2) + ((pos1[1] - pos2[1]) ** 2))

    return dist

def evaluation(dat , parent , p_order , trial , t_order):
    sum_dist , sum_dist_2 = 0 , 0

    # 親の評価
    for i in range(len(parent) - 1):
        sum_dist += distance(dat.ix[parent[i]] , dat.ix[parent[i + 1]])

    sum_dist += distance(dat.ix[parent[len(parent) - 1]] , dat.ix[parent[0]])

    result = np.reciprocal(sum_dist)     # 小さい方が適応度が高いので逆数

    # 子の評価
    for i in range(len(trial) - 1):
        sum_dist_2 += distance(dat.ix[trial[i]] , dat.ix[trial[i + 1]])

    sum_dist_2 += distance(dat.ix[trial[i]] , dat.ix[trial[i + 1]])

    result_trial = np.reciprocal(sum_dist_2)

    # 親と子の比較
    if result > result_trial:
        return result , parent , p_order
    elif result < result_trial:
        return result_trial , trial , t_order
