def main():
    liczba = int(input("Podaj dodatnią liczbę naturalną: "))
    if not liczba >= 0:
        raise ValueError("Liczba miała byc dodatnia")
    licznik = 0
    stara_liczba = liczba
    nowa_liczba = 0
    while liczba > 0:
        cyfra = liczba % 10
        liczba = (liczba - cyfra) / 10
        if cyfra == 0:
            continue
        nowa_liczba = nowa_liczba + cyfra * 10 ** licznik
        licznik = licznik + 1
    print(f"Po pominięciu wszystkich zer w zapisie dziesiętnym liczby {stara_liczba} otrzymamy liczbę {int(nowa_liczba)}.")
    nowy_licznik = 0
    indeks = nowa_liczba
    if indeks > 9:
        while True:
            nowy_licznik += 1
            kolejna_nowa_liczba = indeks
            iloczyn = 1
            while kolejna_nowa_liczba > 0:
                nowa_cyfra = kolejna_nowa_liczba % 10
                kolejna_nowa_liczba = (kolejna_nowa_liczba - nowa_cyfra) / 10
                if nowa_cyfra == 0:
                    continue
                iloczyn = iloczyn * nowa_cyfra
                indeks = iloczyn
            if indeks < 10:
                break
    else:
        nowy_licznik = 1


    print(f"Indeks numerologiczny liczby {stara_liczba} wynosi {int(indeks)}.")
    print(f"Jesteśmy w stanie go obliczyć w {nowy_licznik} krokach.")
if __name__ == "__main__":
    main()