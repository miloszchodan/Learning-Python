import copy
import random

def wypisz_macierz(matrix):
    print(" ", end=" ")
    for column in range(len(matrix[0])):
        if column < 10:
            print(column, end=" ")
        else:
            print(chr(ord("A")+column-10), end=" ")
    print()
    for row in range(len(matrix)):
        if row < 10:
            print(row, end=" ")
        else:
            print(chr(ord("A")+row-10), end=" ")
        for column in range(len(matrix[row])):
            print(f'{matrix[row][column]}', end=" ")
        print()
    print()

def losuj_miny(plansza, liczba_min):
    licznik = 0
    while True:
        x = random.randint(0,len(plansza) - 1)
        y = random.randint(0,len(plansza[0]) - 1)
        if plansza[x][y] == 9:
            continue
        else:
            plansza[x][y] = 9
            licznik += 1
        if licznik == liczba_min:
            break
    return plansza

def wypisz_macierz_cenzura(plansza, cenzura):
    plansza_1 = copy.deepcopy(plansza)
    for i in range(0, len(plansza)):
        for j in range(0, len(plansza[0])):
            if cenzura[i][j] == True:
                continue
            else:
                plansza_1[i][j] = "*"
    return plansza_1

def odkryj_pole(plansza, cenzura, wiersz, kolumna):
    if not 0 <= wiersz <= len(plansza[0]) - 1:
        return False
    if not 0 <= kolumna <= len(plansza) - 1:
        return False
    if plansza[kolumna][wiersz] == 9:
        return False
    else:
        cenzura[kolumna][wiersz] = True
        return True

def numery_przy_minach(plansza):
    for i in range(len(plansza)):
        for j in range(len(plansza[0])):
            if plansza[i][j] == 9:
                continue
            else:
                licznik = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if k == i and j == k:
                            continue
                        elif k < 0 or l < 0 or k > len(plansza) - 1 or l > len(plansza[0]) - 1:
                            continue
                        elif plansza[k][l] == 9:
                            licznik += 1
                        else:
                            continue
                plansza[i][j] = licznik
    return plansza



def main():
    plansza = [[0] * 15 for i in range(10)]
    liczba_min = 15
    plansza = losuj_miny(plansza, liczba_min)
    plansza = numery_przy_minach(plansza)
    cenzura = [[False] * 15 for i in range(10)]
    plansza_1 = wypisz_macierz_cenzura(plansza,cenzura)
    wypisz_macierz(plansza_1)
    while True:
        kolumna = int(input("Podaj wiersz: "))
        wiersz = int(input("Podaj kolumne: "))
        if odkryj_pole(plansza,cenzura,wiersz,kolumna) == False:
            print("PRZEGRAŁEŚ")
            break
        else:
                plansza_1 = wypisz_macierz_cenzura(plansza, cenzura)
                wypisz_macierz(plansza_1)
if __name__ == '__main__':
    main()