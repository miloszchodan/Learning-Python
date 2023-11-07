import random


def mozliwe_akcje():
    print("Mozliwe akcje to: ")
    print("1 - walka")
    print("2 - ucieczka")
    print("3 - cios kung-fu")
    print("4 - zapisz gre")
    print("5 - wczytaj gre")

def wypisz_zycie(zycie):
    print(f"Masz jeszcze {zycie} punktow zycia")

def pobierz_akcje(sila, licznik_atak_3):
    while True:
        akcja = int(input("Podaj akcje: "))
        if not 1 <= akcja <= 5:
            print("Numer akcji musi być pomiędzy 0 a 5")
            continue
        if akcja == 2:
            if sila < 100:
                print("Nie mozesz uciec od straznika posiadajecego mniej niz 100 sily")
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

def zapisz_gre(zycie, zloto, licznik_atak_3):
    plik_do_zapisu = input("Podaj sciezke do zapisu: ")
    with open(plik_do_zapisu, "w") as f:
        f.write(f"{zycie}")
        f.write("\n")
        f.write(str(zloto))
        f.write("\n")
        f.write(str(licznik_atak_3))
        f.write("\n")

def odczytaj_gre():
    plik_do_odczytu = str(input("Podaj sciezke do odczytu: "))
    with open(plik_do_odczytu, "r") as f:
        zycie = int(f.readline())
        zloto = int(f.readline())
        licznik_atak_3 = int(f.readline())
    return zycie, zloto, licznik_atak_3





def main():
    zycie = 500
    zloto = 0
    licznik_atak_3 = 0
    while zycie > 0:
        wypisz_zycie(zycie)
        sila = random.randint(0, 200)
        zloto_chwila = random.randint(0, 200)
        print(f"Goblin o sile {sila} broni {zloto_chwila} sztuk zlota")
        mozliwe_akcje()
        akcja = pobierz_akcje(sila, licznik_atak_3)
        if akcja <= 3:
            if akcja == 1:
                zycie -= random.randint(0, sila)
                zloto += zloto_chwila
            elif akcja == 2:
                if random.random() < 0.20:
                    zycie -= random.randint(0, 2 * sila)
            elif akcja == 3:
                licznik_atak_3 = 4
                zloto += zloto_chwila
            if licznik_atak_3 > 0:
                licznik_atak_3 -= 1
        elif akcja == 4:
            zapisz_gre(zycie, zloto, licznik_atak_3)
        elif akcja == 5:
            zycie, zloto, licznik_atak_3 = odczytaj_gre()
    print("Giniesz!")
    print(f"Udalo Ci sie zebrac {zloto} sztuk zlota")

if __name__ == "__main__":
    main()