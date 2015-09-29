# Import Python libraries
import random as rd
import math
import numpy as np
import pandas as pd
# Coding to include programs
import csvreader as cr
import createdata as cd
import select_rd_inds as sri
import crossover as co
import evaluations as ev
import convert as cv
import cremutant as cm

if __name__ == '__main__':
    individual_path , individual_order , fitness = [] , [] , []
    inds = 100      # 世代あたりの個体数
    gens = 100      # 世代数
    S_factor = 0.5  # Scaling factor

    # Read CSV data and Length of dat
    dat , len_dat = cr.reader()

    # Create individual(1th Generation) : individual_xxx[inds - 1 , len_dat - 1]
    individual_path , individual_order = cd.createind(inds , len_dat)

    f = open('result.csv' , 'w')

    for i in range(gens):
        fitness = [0 for n in range(inds)]
        next_path = np.array([0 for col in range(inds) for row in range(len_dat)]).reshape(inds , len_dat)
        next_order = np.array([0 for col in range(inds) for row in range(len_dat)]).reshape(inds , len_dat)

        # 順番に選択
        for j in range(inds):
            j_path = individual_path[j]
            j_order = individual_order[j]

            # ランダム3つ
            select_path , select_order = sri.select(inds , individual_path , individual_order , j , len_dat)

            # 差分変異親
            mutant_order = np.array(cm.mutant(select_order , S_factor))

            # 交叉して子(Trial)の生成
            trial_order = co.crossover(j_order , mutant_order)
            trial_path = cv.convertOTP(trial_order)

            # 親と子で競争
            fitness[j] , next_path[j] , next_order[j] = ev.evaluation(dat , j_path , j_order , trial_path , trial_order)

        individual_path = next_path
        individual_order = next_order

        print(str(i + 1) + "世代目：" + str(max(fitness)) + "\n" + str(individual_path[fitness.index(max(fitness))]))

        f.write(str(i + 1) + "," + str(max(fitness)) + "\n")

    f.close()
    print(individual_path[fitness.index(max(fitness))])
