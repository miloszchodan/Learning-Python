import random
import math
import copy

def wygeneruj_prosta_sciezke(n):
    lista = [0] * n
    for i in range(0, n):
        lista[i] = i
    return lista

def wygeneruj_miasta_A(n, min_x=-10, max_x=10, min_y=-10, max_y=10):
    x = [0] * n
    y = [0] * n
    for i in range(0, n):
        x[i] = random.uniform(min_x, max_x)
        y[i] = random.uniform(min_y, max_y)
    return x,y

def oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka):
    suma = 0
    for i in range(0, len(sciezka)):
        if i == len(sciezka) - 1:
            suma += math.sqrt((miasta_x[len(sciezka) - 1]- miasta_x[0]) ** 2 + (miasta_y[len(sciezka) - 1]- miasta_y[0]) ** 2)
        else:
            suma += math.sqrt((miasta_x[i] - miasta_x[i + 1]) ** 2 + (miasta_y[i] - miasta_y[i + 1]) ** 2)
    return suma
def znajdz_rozwiazanie_optymalne_A(miasta_x, miasta_y):
    n = len(miasta_x)
    sciezka = wygeneruj_prosta_sciezke(n)
    c = [None] * n
    for i in range(n):
        c[i] = 0
    optymalna_dlugosc = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka)
    optymalna_sciezka = sciezka
    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                sciezka[0], sciezka[i] = sciezka[i], sciezka[0]
            else:
                sciezka[c[i]], sciezka[i] = sciezka[i], sciezka[c[i]]
            dlugosc = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka)
            if dlugosc < optymalna_dlugosc:
                optymalna_dlugosc = dlugosc
                optymalna_sciezka = sciezka
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return optymalna_dlugosc, optymalna_sciezka

def mutuj_A(sciezka, k=3):
    kopia = copy.copy(sciezka)
    n = len(sciezka)
    indeksy = random.sample([i for i in range(n)], k=k)
    wartosc = kopia[indeksy[0]]
    for i in range(k - 1):
        kopia[indeksy[i]] = kopia[indeksy[i + 1]]
    kopia[indeksy[k - 1]] = wartosc
    return kopia

def krzyzuj_A(sciezka1, sciezka2):
    n = len(sciezka1)
    a = random.randint(1, n - 2)
    dziecko = [0] * n
    for i in range(0, a + 1):
        dziecko[i] = sciezka1[i]
    for i in range(a + 1, n):
        dziecko[i] = sciezka2[i - a - 1]
    return dziecko

def main_A():
    random.seed(123)
    n = 7
    min_x, max_x, min_y, max_y = -5, 4, -4, 5

    print("0. Generujemy miasta")
    miasta_x, miasta_y = wygeneruj_miasta_A(n, min_x, max_x, min_y, max_y)
    print(miasta_x)
    print(miasta_y)
    print("\n\n1. Szukamy prostą mutacją")
    sciezka = wygeneruj_prosta_sciezke(n)
    print(f"Prosta sciezka: {sciezka}")
    best_sciezka = sciezka
    best_wartosc = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka)
    print(f"Dla prostej ścieżki długość ścieżki to: {best_wartosc}")
    print(f"mutuj_A([0,1,2,3,4,5,6], 3) = {mutuj_A([0, 1, 2, 3, 4, 5, 6], 3)}")
    print(f"mutuj_A([0,1,2,3,4,5,6], 4) = {mutuj_A([0, 1, 2, 3, 4, 5, 6], 4)}")
    print(f"mutuj_A([0,1,2,3,4,5,6], 5) = {mutuj_A([0, 1, 2, 3, 4, 5, 6], 5)}")

    for i in range(100):
        sciezka_zmutowana = mutuj_A(best_sciezka, 3)
        wartosc = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka_zmutowana)
        if wartosc < best_wartosc:
            best_sciezka = sciezka_zmutowana
            best_wartosc = wartosc
    print(f"Po mutacjach długość ścieżki {best_sciezka} to: {best_wartosc}")
    print("\n\n2. Szukamy przez krzyzowanie")
    sciezka1 = mutuj_A(wygeneruj_prosta_sciezke(n), n - 2)
    sciezka2 = mutuj_A(wygeneruj_prosta_sciezke(n), n - 2)
    wartosc1 = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka1)
    wartosc2 = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka2)
    if wartosc1 > wartosc2:
        sciezka1, sciezka2 = sciezka2, sciezka1
        wartosc1, wartosc2 = wartosc2, wartosc1
    for i in range(1000):
        dziecko = krzyzuj_A(sciezka1, sciezka2)
        wartosc_dziecko = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, dziecko)
        if wartosc1 <= wartosc_dziecko <= wartosc2:
            sciezka2 = dziecko
            wartosc2 = wartosc_dziecko
        elif wartosc_dziecko <= wartosc1:
            sciezka2 = sciezka1
            wartosc2 = wartosc1
            sciezka1 = dziecko
            wartosc1 = wartosc_dziecko
    print(f"\n\nPo krzyżowaniu długość ścieżki {sciezka1} to: {wartosc1}")
    optymalne = znajdz_rozwiazanie_optymalne_A(miasta_x, miasta_y)
    print(f"\n\n3. Optymalny wynik to {optymalne}")
if __name__ == "__main__":
    main_A()