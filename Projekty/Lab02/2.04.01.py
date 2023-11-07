def main():
    liczba = 0
    licznik = 0
    liczba_1 = 0
    licznik_1 = 0
    while True:
        x = int(input("Podaj cyfre 1"))
        if not 0 <= x <= 1:
            break
        liczba = liczba * 10 + x
        licznik += 1
    while True:
        y = int(input("Podaj cyfre 2"))
        if not 0 <= y <= 1:
            break
        liczba_1 = liczba_1 * 10 + y
        licznik_1 += 1
    z = 0
    for i in range(licznik, 0, -1):
        y = liczba // (10 ** i)
        z = y * (2 ** i) + z
        liczba = liczba % 10 ** i
    a = 0
    for j in range(licznik_1, 0, -1):
        y = liczba_1 // (10 ** j)
        a = y * (8 ** j) + a
        liczba_1 = liczba_1 % 10 ** j
    print(f"{z + a}")
    if z > a:
        print("pierwsza")
    elif z < a:
        print("druga")



if __name__ == "__main__":
    main()