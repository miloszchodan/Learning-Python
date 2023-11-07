import math

def main():
    szerokosc = int(input("Podaj szerokosc: "))
    if szerokosc <= 0:
        raise ValueError
    wysokosc = int(input("Podaj wysokosc: "))
    if wysokosc <= 0:
        raise ValueError
    x = float(input("Podaj współrzędną x piłki: "))
    if not 0 <= x <= szerokosc:
        raise ValueError
    y = float(input("Podaj współrzędną y piłki: "))
    if not 0 <= y <= wysokosc:
        raise ValueError
    vx = float(input("Podaj współrzędną x prędkości piłki: "))
    vy = float(input("Podaj współrzędną y prędkości piłki: "))
    t = float(input("Podaj czas symulacji: "))
    if t <= 0:
        raise ValueError
    czas = 0
    while True:
        if vx > 0:
            dx = szerokosc - x
        elif vx < 0:
            dx = x
        if vy > 0:
            dy = wysokosc - y
        elif vy < 0:
            dy = y
        czas_chwilowy = min(dx / math.fabs(vx), dy / math.fabs(vy))
        if czas + czas_chwilowy >= t:
            czas_chwilowy = t - czas
            x += vx * czas_chwilowy
            y += vy * czas_chwilowy
            print(f"Na koniec symulacji piłka znajduje się w punkcie ({x}, {y})")
            break
        x += vx * czas_chwilowy
        y += vy * czas_chwilowy
        czas += czas_chwilowy
        if x == szerokosc or x == 0:
            vx = -vx
            if y == wysokosc or y == 0:
                vy = -vy
        elif y == wysokosc or y == 0:
            vy = -vy
        print(f"Piłka odbiła się w punkcie ({x},{y}) w czasie t={czas}")
    print("Stan planszy po zakończeniu symulacji:")

    for i in range(wysokosc, -1, -1):
        for j in range(0, szerokosc + 1):
            if i == int(y) and j == int(x):
                print("O", end="")
            elif i == wysokosc or i == 0:
                print("#", end="")
            elif j == szerokosc or j == 0:
                print("#", end="")
            else:
                print(" ", end="")
        print("\n")



if __name__ == "__main__":
    main()