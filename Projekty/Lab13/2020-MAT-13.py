import copy


class Samolot:
    __slots__ = ["nazwa", "siedzenia", "liczba_wolnych_miejsc"]

    def __init__(self, nazwa, liczba_rzedow, ile_miejsc_w_rzedzie):
        if liczba_rzedow <= 0 or ile_miejsc_w_rzedzie <= 0:
            raise ValueError("Liczby miejsc i rzedow musza byc dodatnie.")
        self.nazwa = nazwa
        self.siedzenia = [[0] * ile_miejsc_w_rzedzie for i in range(liczba_rzedow)]
        self.liczba_wolnych_miejsc = ile_miejsc_w_rzedzie * liczba_rzedow

    def zamien_litere_na_liczbe(self, litera):
        return ord(litera.upper()) - ord('A')

    def zamien_liczbe_na_litere(self, liczba):
        return chr(liczba + ord('A'))

    def __repr__(self):
        return f"Samolot({self.nazwa}, {len(self.siedzenia)}, {len(self.siedzenia[0])}"

    def __str__(self):
        repr = f"{self.nazwa}\n     "
        for miejsce in range(len(self.siedzenia[0])):
            repr += self.zamien_liczbe_na_litere(miejsce)
        repr += '\n'
        for rzad in range(len(self.siedzenia)):
            repr += f"{rzad + 1}    "
            for miejsce in range(len(self.siedzenia[0])):
                repr +=f"{self.siedzenia[rzad][miejsce]}"
            repr += "\n"
        return repr

    def rozszyfruj_numer_miejsca(self, numer_miejsca):
        miejsce = numer_miejsca[len(numer_miejsca) - 1]
        miejsce = self.zamien_litere_na_liczbe(miejsce)
        rzad = ""
        for i in range(len(numer_miejsca) - 1):
            rzad += numer_miejsca[i]
        rzad = int(rzad) - 1
        return [rzad, miejsce]

    def sprawdz_czy_miejsce_wolne(self, numer_miejsca):
        rzad, miejsce = self.rozszyfruj_numer_miejsca(numer_miejsca)
        return self.siedzenia[rzad][miejsce] == 0

    def rezerwuj_miejsce(self, numer_miejsca):
        rzad, miejsce = self.rozszyfruj_numer_miejsca(numer_miejsca)
        if self.sprawdz_czy_miejsce_wolne(numer_miejsca):
            self.siedzenia[rzad][miejsce] = 1
            self.liczba_wolnych_miejsc -= 1
            return True
        return False

    def ile_wolnych_miejsc(self):
        return self.liczba_wolnych_miejsc

    def skopiuj_samolot_z_rezerwacjami(self, nazwa):
        kopia = Samolot(nazwa, len(self.siedzenia), len(self.siedzenia[0]))
        kopia.siedzenia = copy.deepcopy(self.siedzenia)
        kopia.liczba_wolnych_miejsc = self.liczba_wolnych_miejsc
        return kopia

    def __sub__(self, other):
        if len(self.siedzenia) != len(other.siedzenia) or len(self.siedzenia[0]) != len(other.siedzenia[0]):
            raise ValueError()
        wynik = Samolot(self.nazwa,
                        len(self.siedzenia),
                        len(self.siedzenia[0]))
        for rzad in range(len(self.siedzenia)):
            for miejsce in range(len(self.siedzenia[0])):
                if self.siedzenia[rzad][miejsce] == 1 and other.siedzenia[rzad][miejsce] == 0:
                    wynik.siedzenia[rzad][miejsce] = 1
                    wynik.liczba_wolnych_miejsc -= 1

        return wynik



def main():

    print('--------- ETAP 1 ----------')

    airbus = Samolot('Embraer 190', 5, 4)
    print(airbus)

    print('--------- ETAP 2 ----------')

    print(f"Rezerwacja miejsca 1A zakończkona: {airbus.rezerwuj_miejsce('1A')}")
    print(f"Rezerwacja miejsca 2b zakończkona: {airbus.rezerwuj_miejsce('2b')}")
    print(f"Rezerwacja miejsca 3C zakończkona: {airbus.rezerwuj_miejsce('3C')}")
    print(f"Rezerwacja miejsca 4D zakończkona: {airbus.rezerwuj_miejsce('4D')}")
    print(f"Rezerwacja miejsca 5C zakończkona: {airbus.rezerwuj_miejsce('5C')}")
    print(f"Rezerwacja miejsca 4B zakończkona: {airbus.rezerwuj_miejsce('4B')}")
    print(f"Rezerwacja miejsca 3A zakończkona: {airbus.rezerwuj_miejsce('3A')}")
    print(f"Rezerwacja miejsca 3A zakończkona: {airbus.rezerwuj_miejsce('3A')}")
    assert not airbus.sprawdz_czy_miejsce_wolne('3A'), 'Miejsce dopiero zostało zarezerwowane'
    assert airbus.sprawdz_czy_miejsce_wolne('4C'), 'Miejsce jeszcze nie zostało zarezerwowane'
    print()
    print(airbus)

    print('--------- ETAP 3 ----------')

    print(f'Ilość wolnych miejsc w samolocie to: {airbus.ile_wolnych_miejsc()}')

    print('--------- ETAP 4 ----------')

    airbus_kopia = Samolot.skopiuj_samolot_z_rezerwacjami(airbus, 'Embraer 190+')
    print(airbus_kopia)

    # orginalny obiekt nie powinien ulec zmianie
    print(f"Rezerwacja miejsca 1B zakończkona: {airbus_kopia.rezerwuj_miejsce('1B')}")
    print(f"Rezerwacja miejsca 1C zakończkona: {airbus_kopia.rezerwuj_miejsce('1C')}")
    print(f"Rezerwacja miejsca 1D zakończkona: {airbus_kopia.rezerwuj_miejsce('1D')}")
    assert airbus.sprawdz_czy_miejsce_wolne('1B'), "Kopia się nie udała"
    assert airbus.sprawdz_czy_miejsce_wolne('1C'), "Kopia się nie udała"
    assert airbus.sprawdz_czy_miejsce_wolne('1D'), "Kopia się nie udała"
    print(airbus)
    print(airbus_kopia)

    print('--------- ETAP 5 ----------')

    samolot_z_roznica = airbus_kopia - airbus
    print(samolot_z_roznica)

    samolot_z_roznica.rezerwuj_miejsce('5A')
    assert airbus_kopia.sprawdz_czy_miejsce_wolne('5A'), "Nie powinno się zmienić miejsce oryginalne"


if __name__ == "__main__":
    main()
