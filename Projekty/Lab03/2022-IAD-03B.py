import math

def main():
    cx = float(input("Podaj cx: "))
    cy = float(input("Podaj cy: "))
    x0 = float(input("Podaj x0: "))
    y0 = float(input("Podaj y0: "))
    szerokosc = float(input("Podaj szerokosc: "))
    if szerokosc <= 0:
        raise ValueError
    rozdzielczosc = int(input("Podaj rozdzielczosc: "))
    if rozdzielczosc <= 0 or rozdzielczosc % 2 == 0:
        raise ValueError
    maks_iteracja = int(input("Podaj maksymalną liczbę iteracji dla jednego punktu: "))
    if maks_iteracja < 0:
        raise ValueError
    x = x0
    y = y0
    licznik = 0
    print(f"Trajektoria punktu ({x}, {y}):")
    for i in range(1, maks_iteracja + 1):
        while True:
            odleglosc = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
            if odleglosc > 2:
                break
            x = (x ** 2 - y ** 2 + cx)
            y = (2 * x * y + cy)
            licznik += 1
    x = x0
    y = y0
    licznik_y = y + szerokosc / 2
    licznik_x = x - szerokosc / 2
    while licznik_y >= y - szerokosc / 2:
        while licznik_x <= x + szerokosc / 2:
            for i in range(1, maks_iteracja + 1):
                while True:
                    odleglosc = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
                    if odleglosc > 2:
                        break
                    x = (x ** 2 - y ** 2 + cx)
                    y = (2 * x * y + cy)
                    print("@", end="")
            licznik_x += szerokosc / (rozdzielczosc - 1)
        licznik_y -= szerokosc / (rozdzielczosc - 1)

    print(f"Program wykonał w sumie {licznik} iteracji przekształcenia (x,y)<-(xˆ2 - yˆ2 + {cx}, 2xy + {cy})")
if __name__ == "__main__":
    main()