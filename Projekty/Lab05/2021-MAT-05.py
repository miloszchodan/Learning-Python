import math
import random
import sys
random.seed(20212)

def polowanie(n_swoich, n_rywali, k):
    zdobycz_1 = 0
    zdobycz_2 = 0
    if n_swoich > n_rywali:
        zdobycz_1 += random.randint(30, 50)
        zdobycz_2 += random.randint(5, 20)
    if n_rywali > n_swoich:
        zdobycz_2 += random.randint(30, 50)
        zdobycz_1 += random.randint(5, 20)
    if n_swoich == n_rywali:
        if n_swoich > 0:
            zdobycz_1 += 5
            zdobycz_2 += 5
        elif n_swoich == 0:
            zdobycz_1 += k
            zdobycz_2 += k
    return zdobycz_1, zdobycz_2

def symulacja(p1, p2, n_dni, k):
    licznik_1 = 0
    zdobycze_1 = 0
    zdobycze_2 = 0
    licznik_2 = 0
    for i in range(1, n_dni + 1):
        if licznik_1 >= 2:
            if p1 < random.random():
                wilk_1 = 2
                licznik_1 = 0
            else:
                wilk_1 = 0
                licznik_1 += 1
        else:
            if p1 < random.random():
                wilk_1 = 1
                licznik_1 = 0
            else:
                wilk_1 = 0
                licznik_1 += 1
        if licznik_2 >= 2:
            if p2 < random.random():
                wilk_2 = 2
                licznik_2 = 0
            else:
                wilk_2 = 0
                licznik_2 += 1
        else:
            if p2 < random.random():
                wilk_2 = 1
                licznik_2 = 0
            else:
                wilk_2 = 0
                licznik_2 += 1
        zdobycz_1, zdobycz_2 = polowanie(wilk_1, wilk_2, k)
        zdobycze_1 += zdobycz_1
        zdobycze_2 += zdobycz_2
    return zdobycze_1 / n_dni, zdobycze_2 / n_dni

def p_akaku(t, r):
    p = (1 / (1 + math.exp(-5 * t / (2 * r + 1))))
    return p

def tabela(r, k):
    plik = open("wynik.txt", "w")
    suma = 0
    maks_1 = 0
    maks_2 = 0
    for t1 in range(-r, r + 1):
        p1 = p_akaku(t1, r)
        plik.write(f"p1={p1}\t")
        for t2 in range(-r, r + 1):
            p2 = p_akaku(t2, r)
            srednia_1, srednia_2 = symulacja(p1, p2, 100, k)
            plik.write(f"{srednia_1}, {srednia_2}\t")
            if suma <= srednia_1 + srednia_2:
                maks_1 = srednia_1
                maks_2 = srednia_2
                suma = srednia_1 + srednia_2
    plik.close()
    print(f"Najlepsza suma {maks_1}, {maks_2} ({suma})")


def main():
    while True:
         akcja = int(input(("Co checsz zrobić? (1 - Symulacja, 2 - Tabela, 3 - Koniec): ")))
         if not 1 <= akcja <= 3:
             raise ValueError
         if akcja == 1:
            p1 = float(input("Podaj p1: "))
            p2 = float(input("Podaj p2: "))
            k = int(input("Podaj k: "))
            n_dni = int(input("Podaj liczbę dni: "))
            if not 0 < p1 < 1:
                raise ValueError
            if not 0 < p2 < 1:
                raise ValueError
            if not 0 < k:
                raise ValueError
            if not 0 < n_dni:
                raise ValueError
            zdobycze_1, zdobycze_2 = symulacja(p1, p2, n_dni, k)
            print(f"Stado 1 upolowało {zdobycze_1} zajęcy/dzień, a stado 2 {zdobycze_2} zajęcy/dzień.")
         elif akcja == 2:
             r = int(input("Podaj r: "))
             if not r > 0:
                 raise ValueError
             k = int(input("Podaj k: "))
             if not k > 0:
                 raise ValueError
             tabela(r, k)
         elif akcja == 3:
             break









if __name__ == "__main__":
    main()