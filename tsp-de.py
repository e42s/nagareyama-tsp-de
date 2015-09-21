# Import Python libraries
import random as rd
import math
import numpy as np
import pandas as pd
# Coding to include programs
import csvreader as cr
import createdata as cd
import select_rd_inds as sti
import crossover as co
import evaluation as ev
import convert as cv

if __name__ == '__main__':
    individual_path , individual_order , fitness = [] , [] , []
    inds = 100      # 世代あたりの個体数
    gens = 100      # 世代数
    S_factor = 0.5  # Scaling factor

    # Read CSV data and Length of dat
    dat , len_dat = cr.reader()

    # Create individual(1th Generation) : individual_xxx[inds - 1 , len_dat - 1]
    individual_path , individual_order = cd.createind(inds , len_dat)

    for i in range(gens):
        for j in range(inds):
            j_path = individual_path[j]
            j_order = individual_order[j]

            # ランダム3つ
            select_path , select_order = sti.select(inds , individual_path , individual_order)

            sel_Minus_order = np.array(select_order[1]) - np.array(select_order[2])

            mutant_order = select_order[0] + S_factor * (sel_Minus_order)

            # 交叉して子(Trial)の生成
            trial_order = co.crossover(j_order , mutant_order)
            trial_path = cv.convertOTP(trial_order)

            # 親と子で競争
            fitness = [0 for n in range(inds)]
            fitness[j] , insert_path , insert_order = ev.evaluation(dat , j_path , j_order , trial_path , trial_order)

            # 次世代に入れる
            next_path = np.array([0 for col in range(inds) for row in range(len_dat)]).reshape(inds , len_dat)
            next_order = np.array([0 for col in range(inds) for row in range(len_dat)]).reshape(inds , len_dat)

            next_path[j] = insert_path
            next_order[j] = insert_order

        print(str(j + 1) + "世代目：" + str(max(fitness)))
