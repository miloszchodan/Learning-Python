def main():
    width = 10
    height = int(input("Podaj wysokość ściany {7 ,9 ,11}: "))
    if height < 7 or 7 < height < 9 or 9 < height < 11 or height > 11:
        raise Exception
    x = int(input("Podaj długość rolki `x`: "))
    if x > width - 1 or x <= 0:
        raise Exception
    o = int(input("Podaj długość rolki `o`: "))
    if o > x / 2 or o <= 0:
        raise Exception
    czas_klejenia_x = int(input("Podaj czas klejenia jednej jednostki z rolki `x`: "))
    czas_klejenia_o = czas_klejenia_x / 3
    czas_zmiany = czas_klejenia_x * 3
    print(f"Czas klejenia x= {czas_klejenia_x}, czas klejenia o= {czas_klejenia_o}, czas zmiany rolki= {czas_zmiany}")
    rolka = "o"
    dlugosc_rolki = o
    czas = 0
    rolka_x = 1
    rolka_o = 0
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            if dlugosc_rolki == 0 and rolka == "o":
                rolka = "x"
                dlugosc_rolki = x
                rolka_x += 1
                czas += czas_zmiany
            elif dlugosc_rolki == 0 and rolka == "x":
                rolka = "o"
                dlugosc_rolki = o
                rolka_o += 1
                czas += czas_zmiany
            if i == height - 2 or i == height - 3 or i == height - 4:
                if j == width - 2 or j == width - 3 or j == width - 4:
                    print(" ", end="")
                    continue
            if rolka == "o":
                print("o", end="")
                czas += czas_klejenia_o
            elif rolka == "x":
                print("x", end="")
                czas += czas_klejenia_x
            dlugosc_rolki -= 1
        print("\n")
    print(f"Wytapetowanie całego pokoju zajeło {czas} jednostek czasu")
    print(f"Podczas tapetowania zużyto: {rolka_x} rolek x i {rolka_o} rolek tapety o")

if __name__ == "__main__":
    main()