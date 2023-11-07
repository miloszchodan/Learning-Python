import math
import random
import matplotlib.pyplot as plt



def distance(x, y):
    n = len(x)
    suma = 0
    for i in range(0, n, 1):
        suma += (x[i] - y[i]) ** 2
    odleglosc = math.sqrt(suma)
    return odleglosc

def random_point(n, a=-1, b=1):
    lista = [0] * n
    for i in range(0, n):
        lista[i] = random.uniform(a,b)
    return lista

def volume_exact(n):
    objetosc = (math.pi ** (n / 2)) / math.gamma((n /2) + 1)
    return objetosc

def unit_ball_ratio(n):
    objetosc_kuli = volume_exact(n)
    objetosc_kostki = 2 ** n
    ratio = objetosc_kuli / objetosc_kostki
    return ratio

def volume_approx(n, m=10000):
    lista = [0] * n
    licznik = 0
    for i in range(0, m):
        suma = 0
        for j in range(0, n):
            lista[j] = random.uniform(-1,1)
            suma += (lista[j] ** 2)
        if suma <= 1:
            licznik += 1
    objetosc = (licznik * 2 ** n) / m
    return objetosc

def czas_do_sukcesu(n):
    lista = [0] * n
    licznik = 1
    while True:
        suma = 0
        for j in range(0, n):
            lista[j] = random.uniform(-1,1)
            suma += (lista[j] ** 2)
        if suma <= 1:
            break
        else:
            licznik += 1
    return licznik




def main():
    fig = plt.figure()
    y_exact = [0] * 19
    y_approx = [0] * 19
    y_ratio = [0] * 19
    x = range(1,20)
    for i in range(0, 19):
        y_exact[i] = volume_exact(i + 1)
        y_approx[i] = volume_approx(i + 1)
        y_ratio[i] = unit_ball_ratio(i + 1)
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.scatter(x, y_approx, color="red", marker=(3, 0, 0))
    ax1.scatter(x, y_exact)
    ax1.grid()
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.scatter(x, y_ratio)
    ax2.grid()
    fig.savefig("volume.png", dpi = 90)
    plik = open("czas.txt", "w")
    plik.write(f"n | oczekiwany | przykladowy\n")
    for i in range(1, 16):
        p = unit_ball_ratio(i)
        x = czas_do_sukcesu(i)
        plik.write(f"{i} |\t {1/p} |\t {x}\n")
    plik.close()




if __name__ == "__main__":
    main()



