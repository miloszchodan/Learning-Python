import sys
import math
def main():
    while True:
        print("0 - Sprawdzić czy dwie liczby są lustrzane")
        print("1 - Zakończyć")
        opcja = int(input())
        if opcja == 0:
            break
        elif opcja == 1:
            sys.exit()
        else:
            print("Błędny wybór. Spróbuj jeszcze raz.")
    liczba_1 = int(input("Podaj pierwszą liczbę"))
    liczba_2 = int(input("Podaj drugą liczbę"))
    if not 1 <= liczba_1 < 10 ** 10 or not 1 <= liczba_2 < 10 ** 10:
        raise ValueError
    nowa_liczba_1 = 0
    licznik_1 = 0
    licznik_2 = 0
    while liczba_1 > 0:
        cyfra_1 = liczba_1 % 10
        nowa_liczba_1 = nowa_liczba_1 * 10 + cyfra_1
        liczba_1 = (liczba_1 - cyfra_1) / 10
        licznik_1 += 1
    nowa_liczba_2 = liczba_2
    while liczba_2 > 0:
        cyfra_2 = liczba_2 % 10
        liczba_2 = (liczba_2 - cyfra_2) / 10
        licznik_2 += 1
    if nowa_liczba_1 == nowa_liczba_2:
        print("Liczby mają taką samą liczbę cyfr.")
        print("Podane liczby SĄ liczbami lustrzanymi.")
    else:
        if licznik_2 == licznik_1:
            print("Liczby mają taką samą liczbę cyfr.")
            print("Podane liczby NIE SĄ liczbami lustrzanymi.")
        else:
            print("Liczby mają różną liczbę cyfr.")
            print("Nie mogą to być liczby lustrzane.")

if __name__ == "__main__":
    main()