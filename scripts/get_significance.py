from scipy import stats
import numpy as np
import os


def get_signif(X, Y, i):
    mean1 = np.mean(X)
    mean2 = np.mean(Y)
    if (i == 3):
        print("mean1, mean2: " + str(mean1) + ' ' + str(mean2))
        print(((mean2 - mean1)/mean1) * 100)

    m1 = stats.mannwhitneyu(X, Y, alternative="greater")
    m2 = stats.mannwhitneyu(X, Y, alternative="less")
    m3 = stats.mannwhitneyu(X, Y, alternative="two-sided")

    return (str(m1.statistic) + ',' +  str(m1.pvalue) + ',' +
            str(m2.statistic) + ',' +  str(m2.pvalue) + ',' +
            str(m3.statistic) + ',' +  str(m3.pvalue) + '\n')
    #
    # return (str(stats.mannwhitneyu(X, Y, alternative="greater").pvalue) + "," +
    #       str(stats.mannwhitneyu(X, Y, alternative="less").pvalue) + "," +
    #       str(stats.mannwhitneyu(X, Y, alternative="two-sided").pvalue) + '\n')

def read_file(path, file):
    X = []
    with open("../results/" + path + file + "_final.csv", 'r') as f:
        header = f.readline()
        for line in f:
            data = str.split(line, ',')
            X.append(np.array([float(data[2]), float(data[3]), float(data[4]), float(data[5])]))
    return np.array(X)


def significance(path):
    X = read_file(path, "norm_result")
    Y = read_file(path, "smell_result")

    filename = "../results/signif_" + path.replace('/','_') + ".csv"

    if os.path.exists(filename):
        os.remove(filename)

    with open(filename, 'a') as f:
        f.write("Greater,Lesser,Two-sided\n")

        for i in range(0,4):
            f.write(get_signif(X[:,i], Y[:,i],i))

# significance("python/nbody_0/")
