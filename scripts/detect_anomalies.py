import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN
from matplotlib import pyplot as plt
from kneed import KneeLocator
import os


def plot_cluster(X, m):
    plt.figure(2)
    x1, x2, y, z = [], [], [], []
    for i, c in enumerate(m.labels_):
        if c == -1:
            x1.append(X[i,0])
            y.append(X[i,1])
        else:
            x2.append(X[i,0])
            z.append(X[i,1])
    plt.plot(x1, y, 'rx', x2, z, 'b.')
    plt.title('Total Energy Consumption of Java Nbody 0 original')
    plt.xlabel("Execution Time(ms)")
    plt.ylabel("Total Energy Consumption(kj)")
    plt.legend(["Anomaly", "Cluster"])


def plot_eps(eps, eps2, index, index2, distances):
    # print(d/istances)
    # print(eps, index, eps2, index2)
    dist, x = [], []
    for i in range(len(distances)):
        if (i is not index) and (i is not index2):
            if not(i == index2):
                # print(i, index, index2)
                dist.append(distances[i])
                x.append(i)

    plt.figure(1)
    plt.plot(x, dist, '.')
    plt.title("Optimal eps distance for clustering for Java Nbody 0 original.")
    plt.xlabel("Order from high to low")
    plt.ylabel("Distance to 4th nearest neighbor")

    ylim = plt.ylim()

    plt.plot(index, distances[index], 'rx')
    plt.plot(index2, distances[index2], 'gx')
    plt.legend(["Distances", "Valley", "Knee"])


def get_eps(X):
    neigh = NearestNeighbors(n_neighbors=4)
    nbrs = neigh.fit(X)
    distances, indices = nbrs.kneighbors(X)
    distances = np.sort(distances, axis=0)
    distances = np.flip(distances[:,3])


    slopes = []
    kdist = distances
    for k in range(1, len(kdist)):
        slopes.append(abs(kdist[k]-kdist[k-1]))
    # div = 0.15
    div = 0
    eps = 1
    index = -1
    for l in range(len(slopes)-1):
        if abs(slopes[l] - slopes[l+1]) >= div:
            div = abs(slopes[l] - slopes[l+1])
            eps = kdist[l+1]
            index = l+1

    kneedle = KneeLocator(range(len(distances)), distances, S=1.0, curve='convex', direction='decreasing')
    eps2 = kneedle.knee_y
    plot_eps(eps, eps2, index, kneedle.knee, distances)
    # print(eps, eps2)
    return eps, eps2
    # return eps

def get_dbscan(eps, X):
    m = DBSCAN(eps=eps, min_samples=4)
    m.fit(X)
    return m


def remove_anomalies(path, file):
    X, results = [], []
    with open("../results/" + path + file + ".csv", 'r') as f:
        header = f.readline()
        for line in f:
            results.append(line)
            data = str.split(line, ',')
            X.append(np.array([float(data[1]), float(data[5])]))
    X = np.array(X)

    eps, eps2 = get_eps(X)
    # print(eps, eps2)

    if eps2 is None:
        eps2 = eps

    m = get_dbscan(eps2, X)
    # print(m.labels_)
    # if np.count_nonzero(m.labels_ == -1) > 5:
    #     print(eps, eps2)
    #     m = get_dbscan(eps, X)


    plt.savefig("../results/figures/1Esp_" + path.replace('/', '_') + file + '.svg')
    plot_cluster(X, m)
    # plt.show()
    plt.savefig("../results/figures/1Cluster_" + path.replace('/', '_') +  file + '.svg')


    filename = "../results/" + path + file + "_final.csv"
    if os.path.exists(filename):
        os.remove(filename)

    with open(filename, 'a') as g:
        g.write(header)
        for i in m.core_sample_indices_:
            g.write(results[i])

# remove_anomalies("java/nbody_0/", "norm_result")
