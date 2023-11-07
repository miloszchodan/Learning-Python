import csv

def wczytaj_csv():
    uczestnicy = []
    with open("wyniki_ankiety.csv") as f:
        for row in csv.reader(f):
            uczestnicy.append(row)
    return uczestnicy

def zlicz_odpowiedzi(macierz):
    zliczenie = [[0] * 5 for i in range(0, 3)]
    for i in range(0, len(macierz)):
        for j in range(3, len(macierz[0])):
            if macierz[i][j] == "tak":
                zliczenie[0][j - 3] += 1
            elif macierz[i][j] == "nie":
                zliczenie[1][j - 3] += 1
            elif macierz[i][j] == 'b/o':
                zliczenie[2][j - 3] += 1
    return zliczenie

def narysuj_tabele(zliczenie):
    print(11 * " ","TAK ","NIE ","B/O  ")
    print(27 * "-")
    for i in range(0, len(zliczenie[0])):
        print(f"Pytanie{i}:   {zliczenie[0][i]}   {zliczenie[1][i]}   {zliczenie[2][i]}")

def statystyki(macierz):
    osoby = 0
    for i in range(0,len(macierz)):
        osoby += 1
    print(f"Liczba ankietowanych: {osoby}")
    licznik = 0
    suma_wiek = 0
    for i in range(0, len(macierz)):
        if macierz[i][2] == "":
            continue
        else:
            licznik += 1
            suma_wiek += int(macierz[i][2])
    srednia = suma_wiek / licznik
    srednia = int(srednia * 10) / 10
    print(f"Średnia wieku: {srednia}")
    mezczyzni = 0
    kobiety = 0
    for i in range(0, len(macierz)):
        if macierz[i][1] == "m":
            mezczyzni += 1
        elif macierz[i][1] == "k":
            kobiety += 1
    print(f"Liczba kobiet: {kobiety}")
    print(f"Liczba mezczyzn: {mezczyzni}")


def main():
    uczestnicy = wczytaj_csv()
    zliczenie = zlicz_odpowiedzi(uczestnicy)
    print(zliczenie)
    narysuj_tabele(zliczenie)
    statystyki(uczestnicy)
if __name__ == '__main__':
    main()