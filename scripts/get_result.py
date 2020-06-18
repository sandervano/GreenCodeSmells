import numpy as np
from statistics import mean
import os

# g = open("../results/java/fannkuch_0/norm_0.csv", "r")
def read_file(f):
    X, Y1, Y2, Y3 = [], [], [], []
    for line in f:
        if len(line) < 2:
            continue
        lst = line.split(',')

        X.append(int(lst[0].replace('Kaby Lake', '')))
        Y1.append(float(lst[1]))
        Y2.append(float(lst[2]))
        Y3.append(float(lst[3]))
    return X, Y1, Y2, Y3


def fit_slope(rsX, rsY):
    X, Y = np.array(rsX), np.array(rsY)
    return (((mean(X)*mean(Y)) - mean(X*Y))/((mean(X)*mean(X)) - mean(X*X)))


def analyse_result(X, Y1, Y2, Y3):
    rsX, rsY1, rsY2, rsY3 = [], [], [], []

    minX, minY1, minY2, minY3 = X[0], Y1[0], Y2[0], Y3[0]
    for i, x in enumerate(X):
        y1 = (Y1[i] - minY1)/1000
        if y1 >= 0:
            rsX.append(x-minX)
            rsY1.append(y1)
            rsY2.append((Y2[i] - minY2)/1000)
            rsY3.append((Y3[i] - minY3)/1000)

    slope1, slope2, slope3 = fit_slope(rsX, rsY1), fit_slope(rsX, rsY2), fit_slope(rsX, rsY3)
    return (rsX[-1], rsY1[-1], slope1, rsY2[-1], slope2, rsY3[-1], slope3)


def get_slope(path, id):
    slopes0 = get_wait_slope(path, id + '0')
    slopes1 = get_wait_slope(path, id + '1')

    return [(slopes0[i] + slopes1[i])/2 for i in (0,1,2)]


def get_wait_slope(path, id):
    wait = open("../results/" + path + 'wait_' + id + '.csv', 'r')
    results = [*read_file(wait)]
    wait.close()
    # print(len(results))
    return [fit_slope(results[0], results[i]) for i in (1,2,3)]


def get_results(path, id):
    wait_slope = get_slope(path, id)

    filename = "../results/" + path + id + 'result.csv'
    if os.path.exists(filename):
        os.remove(filename)

    with open(filename, 'a') as f:
        f.write('id,time,package0,pp0,dram,total\n')

        for i in range(0, 50):
            g = open("../results/" + path + id + str(i) + '.csv', 'r')

            results = analyse_result(*read_file(g))
            g.close()
            x = results[0]

            y1 = results[1] - wait_slope[0] * x
            w1 = results[2] - wait_slope[0]
            y2 = results[3] - wait_slope[1] * x
            w2 = results[4] - wait_slope[1]
            y3 = results[5] - wait_slope[2] * x
            w3 = results[6] - wait_slope[2]

            f.write(str(i) + ',' + str(x) + ',' + str(y1)+ ',' + str(y2) + ',' + str(y3) + ',' + str(y1 + y3) + '\n')
