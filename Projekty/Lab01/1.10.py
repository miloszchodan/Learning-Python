def main():
    cena = float(input("Podaj cene"))
    spalanie = float(input("Podaj spalanie"))
    hajs = int(input("Podaj ilosc pieniedzy"))
    dystans = int(input("Podaj ilosc kilometrow"))
    if cena <= 0 or 3 <= spalanie <= 50 or hajs < 0 or dystans < 0:
        zasieg = (hajs * 100) / (spalanie * cena)
        koszt = cena / (100 * spalanie)
        print(f"Koszt przejechania 1km to {koszt}")
        if dystans <= zasieg:
            print("Możesz jechac!")
        else:
            print(f"Niestety brakuje Ci {(dystans-zasieg)/koszt} zl.")


if __name__ == "__main__":
    main()