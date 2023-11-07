import random

def mozliwe_akcje():
    print("Mozliwe akcje to:")
    print("1 - atak toporem(230 obrazen, 30 % szan na trafienie)")
    print("2 - magiczny pocisk(50 - 100 obrazen, 20 punktow many)")
    print("3 - potezny atak(200 - 400 obrazen, 35 % szans na trafienie, raz na cztery tury)")
    print("4 - zapisz grę")
    print("5 - odczytaj grę")

def wypisz_zycie_trolla(zycie):
    print(f"Troll ma {zycie} pkt zycia")


def pobierz_akcje(mana, licznik_atak_3):
    while True:
        akcja = int(input("Podaj akcje: "))
        if not 1 <= akcja <= 5:
            print("Numer akcji musi być pomiędzy 0 a 5")
            continue
        if akcja == 2:
            if mana < 20:
                print("Za mało many.")
                continue
            else:
                return akcja
        elif akcja == 3:
            if licznik_atak_3 > 0:
                print("Jeszcze za wcześnie na atak 3")
                continue
            else:
                return akcja
        else:
            return akcja


def zapisz_gre(zycie, mana, licznik_atak, licznik_atak_3):
    plik_do_zapisu = input("Podaj sciezke do zapisu: ")
    with open(plik_do_zapisu, "w") as f:
        f.write(f"{zycie}")
        f.write("\n")
        f.write(str(mana))
        f.write("\n")
        f.write(str(licznik_atak))
        f.write("\n")
        f.write(str(licznik_atak_3))
        f.write("\n")


def odczytaj_gre():
    plik_do_odczytu = str(input("Podaj sciezke do odczytu: "))
    with open(plik_do_odczytu, "r") as f:
        zycie = int(f.readline())
        mana = int(f.readline())
        licznik_atak = int(f.readline())
        licznik_atak_3 = int(f.readline())
    return zycie, mana, licznik_atak, licznik_atak_3


def main():
    zycie = 1000
    mana = 100
    licznik_atak = 0
    licznik_atak_3 = 0
    while zycie > 0:
        wypisz_zycie_trolla(zycie)
        mozliwe_akcje()
        akcja = pobierz_akcje(mana, licznik_atak_3)
        if akcja <= 3:
            if akcja == 1:
                a = random.random()
                if a <= 0.3:
                    zycie -= 230
            elif akcja == 2:
                b = random.randint(50, 100)
                zycie -= b
                mana -= 20
            elif akcja == 3:
                c = random.randint(200, 400)
                zycie -= c
                licznik_atak_3 = 4
            if licznik_atak_3 > 0:
                licznik_atak_3 -= 1
            licznik_atak += 1
        elif akcja == 4:
            zapisz_gre(zycie, mana, licznik_atak, licznik_atak_3)
        elif akcja == 5:
            zycie, mana, licznik_atak, licznik_atak_3 = odczytaj_gre()
    print(f"Udalo Ci sie pokonac trolla w {licznik_atak} atakach")

if __name__ == "__main__":
    main()