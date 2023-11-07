import numpy as np
from sklearn import datasets, svm

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def F(a, b):
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    X, y = X[y != 0, :2], y[y != 0]
    n_sample = len(X)
    np.random.seed(1234)
    order = np.random.permutation(n_sample)
    X = X[order]
    y = y[order].astype(np.float)
    X_train = X[:int(0.8 * n_sample)]
    y_train = y[:int(0.8 * n_sample)]
    X_test = X[int(0.8 * n_sample):]
    y_test = y[int(0.8 * n_sample):]
    clf = svm.SVC(gamma=a, C=b)
    clf.fit(X_train, y_train)
    return np.mean(clf.predict(X_test) == y_test)
def main():
    input_file = open("input.txt", "r")
    a1 = float(input_file.readline())
    an = float(input_file.readline())
    n = int(input_file.readline())
    b1 = float(input_file.readline())
    bm = float(input_file.readline())
    m = int(input_file.readline())
    r = (an - a1) / (n - 1)
    p = (bm - b1) / (m - 1)
    if a1 > an or b1 > bm or m < 1 or n < 1:
        raise ValueError
    output_file = open("output.txt", "w")
    output_file.write("a \ b ")
    output_file.write("| ")
    for i in range(1, m+1):
        bi = b1 + (i - 1) * p
        output_file.write(f"{bi} ")
    output_file.write("\n")
    output_file.write("-----")
    output_file.write("|")
    for i in range(1, 37):
        output_file.write("-")
    output_file.write("\n")
    f_max = 0
    f_min = 1
    for i in range(1, n+1):
        ai = a1 + (i - 1) * r
        output_file.write(f"{ai} ")
        output_file.write("|")
        for j in range(1, m+1):
            bj = b1 + (j - 1) * p
            output_file.write(f"{F(ai, bj)} ")
            if F(ai, bj) >= f_max:
                f_max = F(ai, bj)
                a_max = ai
                b_max = bj
            if F(ai, bj) <= f_min:
                f_min = F(ai, bj)
                a_min = ai
                b_min = bj
        output_file.write("\n")
    print(f"fmax= {f_max}")
    print(f"fmin= {f_min}")
    print(f"Para dla f_max to {a_max, b_max}")
    output_file.close()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([a1, an])
    ax.set_ylim([b1, bm])
    for i in range(1,n+1):
        ai = a1 + (n - 1) * r
        for j in range(1, m + 1):
            bj = b1 + (j - 1) * p
            ax.add_patch(patches.Rectangle(
                (ai, bj),
                r,
                p,
                facecolor=str(1 - 0.3)
            ))


    fig.savefig('output.png', dpi=90)








if __name__ == "__main__":
    main()
