


def main():
    liczba = int(input("Podaj liczbę całkowitą większą niż 1: "))
    if liczba <= 0:
        raise ValueError
    print(f"Dzieliniki liczby {liczba} to: ")
    liczba_1 = liczba
    dzielnik = 2
    licznik = 1
    iloczyn = 1
    maks_licznik = 1
    while liczba > 1:
        if liczba % dzielnik == 0:
            liczba = liczba / dzielnik
            if licznik == 1:
                print(dzielnik)
                iloczyn = iloczyn * dzielnik
            licznik += 1
            if maks_licznik < licznik:
                maks_licznik = licznik - 1
                maks_dzielnik = dzielnik


        else:
            dzielnik += 1
            licznik = 1
    print(f"W rozkladzie {liczba_1} na czynniki pierwsze najczęściej pojawia się {maks_dzielnik}, występuje {maks_licznik} razy.")
    print(f"Jeżeli w rozkładzie {liczba_1} na czynniki pierwsze pominiemy krotności, otrzymamy liczbę {iloczyn}.")


if __name__ == "__main__":
    main()