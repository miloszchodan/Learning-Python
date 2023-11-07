import math

def main():
    licznik = 0
    licznik_1 = 0
    while True:
        x = math.nan
        y = x
        x = int(input("Podaj x"))
        if x < 0:
            break
        if x > y:
            raise Exception("Bledne dane")
        licznik += 1
        if x < licznik:
            licznik_1 += 1
    print(f"{licznik}")
    print(f"{licznik-licznik_1}")



if __name__ == "__main__":
    main()