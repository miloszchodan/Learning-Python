import math
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def generate_fractal(n):
    Z = [[0] * n for i in range(2)]
    Z[0][0] = 0
    Z[1][0] = 0
    for i in range(1, n):
        if random.uniform(0,1) < 0.32:
            Z[0][i] = -0.67 * Z[0][i - 1] - 0.02 * Z[1][i - 1]
            Z[1][i] = -0.18 * Z[0][i - 1] + 0.81 * Z[1][i - 1] + 10
        elif 0.32 <= random.uniform(0,1) < 0.64:
            Z[0][i] = 0.4 * Z[0][i - 1] + 0.4 * Z[1][i - 1]
            Z[1][i] = -0.1 * Z[0][i - 1] + 0.4 * Z[1][i - 1]
        elif 0.64 <= random.uniform(0,1) < 0.96:
            Z[0][i] = -0.4 * Z[0][i - 1] - 0.4 * Z[1][i - 1]
            Z[1][i] = -0.1 * Z[0][i - 1] + 0.4 * Z[1][i - 1]
        else:
            Z[0][i] = -0.1 * Z[0][i - 1]
            Z[1][i] = 0.44 * Z[0][i - 1] + 0.44 * Z[1][i - 1] - 2
    x_min = min(Z[0])
    x_max = max(Z[0])
    y_min = min(Z[1])
    y_max = max(Z[1])
    for i in range(len(Z[0])):
        Z[0][i] = (Z[0][i] - x_min) / (x_max - x_min)
        Z[1][i] = (Z[1][i] - y_min) / (y_max - y_min)
    return Z

def find_box_id(x, y, eps):
    n = math.ceil(1 / eps)
    boxes = []
    for i in range(n):
        for j in range(n):
            for k in range(len(x)):
                if i * eps <= x[k] < (i + 1) * eps and j * eps <= y[k] < (j + 1) * eps:
                    boxes.append([i, j])
                    break
    return boxes


def unique_boxes(boxes):
    lista = []
    for i in range(len(boxes)):
        for j in range(len(lista)):
            if boxes[i] == lista[j]:
                break
            lista.append(boxes[i])
    n = len(lista)
    return n

def fractal_dimension(x, y, eps):
    boxes = find_box_id(x, y, eps)
    n = unique_boxes(boxes)
    d = math.log(n, 1 / eps)
    return d






def main():
    random.seed(123)
    n = int(1e6)
    Z = generate_fractal(n)
    x = Z[0]
    y = Z[1]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.scatter(x, y, marker=".", s=1, color="forestgreen")
    fig.savefig("zadanie_5_p1_points.png")
    eps = 0.13
    tree_box = find_box_id(x, y, eps)
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    plt.scatter(x, y, marker=".", s=1, color="forestgreen")
    for i in set([tuple(x) for x in tree_box]):
        ax.add_patch(patches.Rectangle((i[0] * eps, i[1] * eps), eps, eps, alpha=0.5, facecolor="gray", edgecolor="black"))
        mark = "(" + str(i[0]) + "," + str(i[1]) + ")"
        ax.annotate(mark, xy=(i[0] * eps + 0.25 * eps, i[1] * eps + 0.25 * eps))
    plt.savefig("zadanie_5_p1_boxes.png")
    epss = []
    eps_0 = 0.005
    for i in range(20):
        eps_chwilowy = (i + 1) * eps_0
        epss.append(eps_chwilowy)
    print(epss)
    dims = []
    for i in range(20):
        dim = fractal_dimension(x, y, epss[i])
        dims.append(dim)
    print(dims)
    fig = plt.figure(2)
    ax = fig.add_subplot(111)
    ax.set_xlim([-0.01, 0.11])  # zakres wartości na osi OX
    ax.scatter(epss, dims)
    fig.savefig("zadanie_5_p1_dimension.png")
    fig = plt.figure(3)
    ax = fig.add_subplot(1, 1, 1, facecolor='midnightblue')
    ax.set_xlim([-0.1, 1.1])
    ax.set_ylim([-0.1, 1.1])
    ax.scatter(x, y, marker=".", s=1, color="forestgreen")
    y_max = max(y)
    indeks = y.index(y_max)
    ax.scatter(x[indeks], y[indeks], marker="*", s=500, color="gold")
    x_bombki = random.sample(x, 30)
    y_bombki = random.sample(y, 30)
    colors = ["firebrick", "coral", "magenta", "indianred", "orange"] * 6
    ax.scatter(x_bombki, y_bombki, marker="o", s=200, color=colors)
    x_snow = []
    y_snow = []
    for i in range(500):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        x_snow.append(x)
        y_snow.append(y)
    ax.scatter(x_snow, y_snow, marker="o", s=10, color="ivory", alpha=0.6)
    fig.savefig("zadanie_5_p1_choinka.jpg", dpi=90)








if __name__ == '__main__':
    main()