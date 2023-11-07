import random
random.seed(123)
import math
import matplotlib.pyplot as plt

def regresja(x, y):
    suma_x = 0
    suma_y = 0
    n = len(x)
    for i in range(0, n, 1):
        suma_x += x[i]
        suma_y += y[i]
    srednia_x = suma_x / n
    srednia_y = suma_y / n
    licznik = 0
    mianownik = 0
    for i in range(0, n, 1):
        licznik += (x[i] - srednia_x) * (y[i] - srednia_y)
        mianownik += (x[i] - srednia_x) ** 2
    beta = licznik / mianownik
    alfa = srednia_y - beta * srednia_x
    return alfa, beta, x, y

def E(alfa, beta, x, y):
    suma = 0
    n = len(x)
    for i in range(0, n, 1):
        suma += (alfa + beta * x[i] - y[i]) ** 2
    return suma

def r(x, y):
    suma_x = 0
    suma_y = 0
    n = len(x)
    for i in range(0, n, 1):
        suma_x += x[i]
        suma_y += y[i]
    srednia_x = suma_x / n
    srednia_y = suma_y / n
    suma_s_x = 0
    suma_s_y = 0
    for i in range(0, n, 1):
        suma_s_x += (x[i] - srednia_x) ** 2
        suma_s_y += (y[i] - srednia_y) ** 2
    s_x = math.sqrt(suma_s_x / n)
    s_y = math.sqrt(suma_s_y - srednia_y)
    suma = 0
    for i in range(0, n, 1):
        suma += ((x[i] - srednia_x) * (y[i] - srednia_y)) / (s_x * s_y)
    r = suma / (n - 1)
    return r











def main():
    alpha0 = -3
    beta0 = 1.5
    n = 100
    x = [random.uniform(-10, 10) for i in range(n)]
    y = [alpha0 + beta0 * x[i] + random.normalvariate(0, 1) for i in range(n)]
    plt.scatter(x, y)
    plt.plot([-10, 10], [alpha0 + beta0 * (-10), alpha0 + beta0 * 10], color="red")
    plt.savefig("zadanie_6_01.png")


if __name__ == "__main__":
    main()