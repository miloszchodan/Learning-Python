def main():
    liczba = 0
    licznik = 0
    while True:
        if liczba >= 10**20:
            break
        x = int(input("Podaj cyfre"))
        if not 0 <= x <= 7:
            break
        liczba = liczba + x * 10 ** licznik
        licznik += 1
    print(f"{liczba}")
    z = 0
    for i in range(licznik, 0, -1):
        y = liczba // (10 ** i)
        z = y * (8 ** i) + z
        liczba = liczba % 10 ** i
    print(f"{z}")




if __name__ == "__main__":
    main()