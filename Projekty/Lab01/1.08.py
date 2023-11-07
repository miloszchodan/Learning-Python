import sys


def main():
    x = float(input("Podaj dlugosc"))
    y = float(input("Podaj szerokosc"))
    z = float(input("Podaj wysokosc"))
    if x <= 0 or y <= 0 or z <= 0:
        print("Bledne dane")
        sys.exit()
    ilosc_rolek = ((2*x*z)+(2*y*z))/2.548
    if ilosc_rolek > 400:
        koszt = ilosc_rolek * 1.37 + 100
    else:
        koszt = ilosc_rolek * 1.37
    print(f"Zeby szczelnie owinac budynek potrzeba {ilosc_rolek} rolek papieru")
    print(f"Ten papier bedzie kosztowac {koszt}")

if __name__ == "__main__":
    main()