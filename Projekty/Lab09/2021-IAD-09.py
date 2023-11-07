import csv
def wczytaj_dane(sciezka):
    M = []
    f = open(sciezka)
    for row in csv.reader(f):
        for i in range(len(row)):
            row[i] = int(row[i]) # konwersja z str na int
        list.append(M, row) # == A.append(row)
    f.close()
    return M

def wypisz(dane):
    print("  ", end=" ")
    for column in range(len(dane[0])):
        print(column, end=" ")
    print()
    for row in range(len(dane)):
        print(f"{row}:", end=" ")
        for column in range(len(dane[row])):
            print(f'{dane[row][column]}', end=" ")
        print()
    print()

def szukaj_bezpiecznych_dan(dane, lista):
    licznik = 0
    for i in range(len(dane)):
        alergeny = 0
        for j in range(len(lista)):
            alergeny += dane[i][lista[j]]
        if alergeny == 0:
            licznik += 1
        else:
            continue
    dania = [0] * licznik
    nowy_licznik = 0
    for i in range(len(dane)):
        alergeny_1 = 0
        for j in range(len(lista)):
            alergeny_1 += dane[i][lista[j]]
        if alergeny_1 == 0:
            dania[nowy_licznik] = i
            nowy_licznik += 1
        else:
            continue
    return dania

def dodaj_nowe_danie(dane, lista):
    M = [[0] * len(dane[0]) for i in range(len(dane) + 1)]
    for i in range(len(dane)):
        for j in range(len(dane[0])):
            M[i][j] = dane[i][j]
    for i in range(len(dane[0])):
        for j in range(len(lista)):
            if i == lista[j]:
                M[len(dane)][i] = 1
            else:
                continue
    return M

def usun_najgorsze(dane, k):
    licznik_dan = 0
    lista = [0] * len(dane)
    for i in range(len(dane)):
        licznik = 0
        for j in range(len(dane[0])):
            licznik += dane[i][j]
        lista[i] = licznik
        if licznik < k:
            licznik_dan += 1
        else:
            continue
    M = [[0] * len(dane[0]) for i in range(licznik_dan)]
    licznik_wierszy = 0
    for i in range(len(dane)):
        if lista[i] < k:
            M[licznik_wierszy] = dane[i]
            licznik_wierszy += 1
    return M

def zapisz_informacje(dane, sciezka):
    plik = open(sciezka, "w")
    plik.write(f"liczba dan: {len(dane)}\n")
    plik.write(f"liczba uwzglednionych alergenow: {len(dane[0])}\n")
    for i in range(0,len(dane)):
        maks = 0
        licznik = 0
        for j in range(len(dane[0])):
            licznik += dane[i][j]
        if licznik >= maks:
            maks = licznik
    lista = [0] * (maks + 1)
    for i in range(len(dane)):
        licznik = 0
        for j in range(len(dane[0])):
            licznik += dane[i][j]
        lista[licznik] += 1
    plik.write(f"maksymalna liczba alergenow w jednym daniu: {len(lista)}\n")
    for i in range(len(lista)):
        plik.write(f"liczba dan z {i} alergenami: {lista[i]}\n")
    plik.close()

def main():
    sciezka = "alerg.csv"
    M = wczytaj_dane(sciezka)
    wypisz(M)
    print(szukaj_bezpiecznych_dan(M, [0, 5, 10]))
    M = dodaj_nowe_danie(M, [1, 2, 3, 8])
    wypisz(M)
    M = usun_najgorsze(M, 5)
    wypisz(M)
    zapisz_informacje(M, "zapis.txt")
if __name__ == '__main__':
    main()