import matplotlib.pyplot as plt
import numpy as np
names = ["Package0", "PP0", "DRAM", "P0+DRAM"]

def read_file(name, file):
    X = []
    with open("../results/" + name + file + ".csv", 'r') as f:
        header = f.readline()
        for line in f:
            data = str.split(line, ',')
            X.append(np.array([float(data[1]), float(data[2]), float(data[3]), float(data[4]), float(data[5])]))
    return np.array(X)

def plot_result(path, X, Y):
    for i in range(1,5):
        plt.figure(i)
        plt.plot(X[:,0], X[:,i], '.', Y[:,0], Y[:,i], '.')
        plt.title("Total Energy consumption of " + path.replace('/', ' ') + "for " + names[i-1])
        plt.ylabel("Total Energy consumption(kj)")
        plt.xlabel("Execution Time(ms)")
        plt.legend(["Normal", "Smelly"])

        plt.savefig("../results/figures/TEnergy_" + path.replace('/', '_') + names[i-1] + '.svg')

def plot_bar(path, X, Y):
    plt.figure(7)
    plt.boxplot([X[:,0], Y[:,0]], labels=["Original", "Smelly"])

    plt.title("Total Execution Time of " + path.replace('/', ' '))
    plt.ylabel("Total Execution Time(ms)")
    plt.xlabel("Type of software project")

    plt.savefig("../results/figures2/BoxPlotT_" + path.replace('/', '_') + '.svg')
    # plt.show()

def plot_results(path):
    X = read_file(path, "norm_result_final")
    Y = read_file(path, "smell_result_final")

    # plot_result(path, X, Y)
    plot_bar(path, X, Y)
