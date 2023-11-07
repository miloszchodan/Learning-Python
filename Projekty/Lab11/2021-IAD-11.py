import matplotlib.pyplot as plt
import math
import numpy
from PIL import Image

def narysuj_wielokat(lista_wierzcholkow):
    x = []
    y = []
    for p in lista_wierzcholkow:
        x.append(p[0])
        y.append(p[1])
    x.append(lista_wierzcholkow[0][0])
    y.append(lista_wierzcholkow[0][1])
    plt.axis('equal')
    plt.plot(x, y)
    plt.show()



def png_write(img):
    img = Image.fromarray((numpy.array(img) * 255).astype(numpy.int8), 'L')
    img.save("output.png")

def trzeci_punkt_trojkata_rownobocznego(p1, p2):
    odleglosc = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    srodek = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    kat = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    wynik_x = srodek[0] - odleglosc * 3 ** 0.5 / 2 * math.sin(kat)
    wynik_y = srodek[1] + odleglosc * 3 ** 0.5 / 2 * math.cos(kat)
    return wynik_x, wynik_y

def kolejna_iteracja(lista):
    n = len(lista)
    punkty = [[0, 0] for i in range(4 * n)]
    for i in range(len(lista)):
        punkty[4 * i] = lista[i]
        a, b = lista[i]
        if i == len(lista) - 1:
            c, d = lista[0]
        else:
            c, d = lista[i + 1]
        dx = a - c
        dy = b - d
        punkty[4 * i + 1] = c + 2 * dx / 3, d + 2 * dy / 3
        punkty[4 * i + 3] = c + dx / 3, d + dy / 3
        punkty[4 * i + 2] = trzeci_punkt_trojkata_rownobocznego(punkty[4 * i + 3], punkty[4 * i + 1])
    return punkty

def odleglosc(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

def podpodzial(wielokat):
    wynik = []
    for i in range(len(wielokat)):
        pcur = wielokat[i]
        pnext = wielokat[(i + 1) % len(wielokat)]
        n = math.ceil(odleglosc(pcur, pnext))
        for j in range(n):
            x = (j * pcur[0] + (n - j) * pnext[0]) / n
            y = (j * pcur[1] + (n - j) * pnext[1]) / n
            wynik.append((x, y))
    return wynik

def wypelniony_wielokat(wielokat, punkt):
    wielokat = podpodzial(wielokat)
    minx, maxx, miny, maxy = int(wielokat[0][0]), int(wielokat[0][0]), int(wielokat[0][1]), int(wielokat[0][1])
    for p in wielokat:
        x, y = int(p[0]), int(p[1])
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y
    macierz = [[0] * (maxy - miny + 1) for _ in range(maxx - minx + 1)]
    for p in wielokat:
        x, y = int(p[0]), int(p[1])
        macierz[x - minx][y - miny] = 1
    punkty = [(int(punkt[0]) - minx, int(punkt[1]) - miny)]
    nastepny_do_odwiedzenia = 0
    while nastepny_do_odwiedzenia < len(punkty):
        x, y = punkty[nastepny_do_odwiedzenia]
        nastepny_do_odwiedzenia += 1
        if macierz[x][y] == 1:
            continue
        macierz[x][y] = 1
        for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x + i < len(macierz) and 0 <= y + j < len(macierz[0]) and macierz[x + i][y + j] == 0:
                punkty.append((x + i, y + j))
    return macierz






def platek_sniegu_Kocha(d):
    p1 = [0, 0]
    p2 = [0, d]
    p3 = trzeci_punkt_trojkata_rownobocznego(p1, p2)
    lista = [p1, p2, p3]
    for i in range(10):
        lista = kolejna_iteracja(lista)
        narysuj_wielokat(lista)
        png_write(wypelniony_wielokat(lista, (0, 3)))

def main():
    d = 200
    platek_sniegu_Kocha(d)



if __name__ == '__main__':
    main()