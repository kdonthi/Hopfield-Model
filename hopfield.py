import pandas as pd
import random as rand
import matplotlib.pyplot as plt
import sys


def weightMatrix(dim, symmetric):
    df = pd.DataFrame(index=list(range(dim)), columns=list(range(dim)))
    if symmetric == 0:
        for i in range(dim):
            for j in range(dim):
                df.iloc[i][j] = rand.randint(-10, 10)
    elif symmetric == 1:
        diagonalnum = rand.randint(-10, 10)
        startnum = 0
        for i in range(dim):
            for j in range(startnum, dim):
                if (i == j):
                    df.iloc[i][j] = diagonalnum
                elif j > i:
                    df.iloc[i][j] = rand.randint(-10, 10)
                else:
                    print("error")
                    exit()
            startnum += 1
        endnum = 0
        for i in range(dim):
            for j in range(0, endnum):
                # symmettric indices should already be filled
                df.iloc[i, j] = df.iloc[j, i]
            endnum += 1

    print("Weights:")
    print(df)
    return (df)


def energyValue(X, wMatrix, thetas):
    energy = (X.T).dot(wMatrix)
    energy = energy.dot(X)
    energy += (thetas.T).dot(X)
    return (energy.iloc[0][0])


def update(iterations, wMatrix, X, thetas, plottype):
    dictionary = {"x": [], "y": []}
    n = X.size
    index = 0
    for i in range(iterations):
        dictionary["x"].append(i + 1)
        dictionary["y"].append(energyValue(X, wMatrix, thetas))
        if plottype == "synch":
            X = wMatrix.dot(X) - thetas
            X = X > 0  # Heaviside function
        elif plottype == "asynchrand":
            index = rand.randint(0, n - 1)  # choosing random neuron to update
        elif plottype == "asynchorder":
            index = i % n  # choosing indexes of neuron in order
        if plottype == "asynchrand" or plottype == "asynchorder":
            X[index] = (wMatrix.iloc[index, :]).dot(X) - thetas.iloc[index, 0]
            X[index] = X[index] > 0
    df = pd.DataFrame(dictionary)
    print("Iteration vs Energy")
    print(df)
    df.plot(x="x", y="y")
    plt.show()


def main():
    assert(len(sys.argv) == 4)
    plottype = sys.argv[1]
    dim = sys.argv[2]
    symmetric = sys.argv[3]
    assert(plottype == "synch" or plottype ==
           "asynchrand" or plottype == "asynchorder")
    for i in dim:
        assert(ord(i) >= 48 and ord(i) <= 57)
    assert(symmetric == '0' or symmetric == '1')
    dim = int(dim)
    symmetric = int(symmetric)
    iterations = 100

    X = []
    for i in range(dim):
        X.append(rand.randint(0, 1))
    dfX = pd.DataFrame(X)
    print("Inital X values:")
    print(dfX)
    wMatrix = weightMatrix(dim, symmetric)

    thetas = []
    for i in range(dim):
        thetas.append(1)
    dfthetas = pd.DataFrame(thetas)

    print("Thetas:")
    print(dfthetas)
    update(iterations, wMatrix, dfX, dfthetas, plottype)
    print("Type as an argument, synch, asynchrand, or asynchorder, and then one dimension of the weight matrix, e.g. python3 hopfield.py synch 3")


main()
