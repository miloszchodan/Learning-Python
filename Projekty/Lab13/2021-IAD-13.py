class Zamowienie:
    __slots__ = ['towary']
    ceny = [i + 1 for i in range(21)]

    def __init__(self, lista = None):
        if lista == None:
            self.towary = []
        else:
            max = 0
            for i in range(len(lista)):
                if not 0 <= lista[i][0] <= 20:
                    raise Exception()
                if type(lista[i][0]) != int:
                    raise Exception()
                if type(lista[i][1]) != int:
                    raise Exception()
                if lista[i][1] < 0:
                    raise Exception()
                if lista[i][0] > max:
                    max = lista[i][0]
            self.towary = [0] * (max + 1)
            for i in range(len(lista)):
                self.towary[lista[i][0]] = lista[i][1]

    def __repr__(self):
        return f"Zamowienie(towary = {self.towary})"

    def __str__(self):
        towar = "towar:"
        sztuk = "sztuk:"
        for i in range(len(self.towary)):
            towar += f"{i:3d}"
            sztuk += f"{self.towary[i]:3d}"
        return f"{towar}\n{sztuk}"

    def oblicz_wartosc(self):
        suma = 0
        for i in range(len(self.towary)):
            suma += self.towary[i] * Zamowienie.ceny[i]
        return suma

    def __lt__(self, other):
        if type(other) != Zamowienie:
            raise Exception()
        if self.oblicz_wartosc() < other.oblicz_wartosc():
            return True
        else:
            return False

    def __add__(self, other):
        if type(other) == Zamowienie:
            l = max(len(self.towary), len(other.towary))
            lista = [0] * l
            for i in range(len(self.towary)):
                lista[i] += self.towary[i]
            for i in range(len(other.towary)):
                lista[i] += other.towary[i]
        elif type(other) == tuple:
            if len(other) != 2:
                raise Exception()
            if other[0] > len(self.towary):
                lista = [0] * (other[0] + 1)
            else:
                lista = [0] * len(self.towary)
            for i in range(len(self.towary)):
                lista[i] += self.towary[i]
            lista[other[0]] += other[1]
        else:
            raise Exception()
        return lista








def main():
    ##################### ETAP1 #####################
    print("## ETAP1: STWORZENIE KLASY, KONSTRUKTOR (2 PUNKTY) ##")
    zamowienie1 = Zamowienie([(1, 9), (3, 5), (4, 2), (7, 4), (0, 1)])
    zamowienie2 = Zamowienie([(0, 5), (4, 7), (19, 8), (7, 1)])
    zamowienie3 = Zamowienie()
    print(zamowienie1.towary)
    print(zamowienie2.towary)
    print(zamowienie3.towary)

    ##################### ETAP2 #####################
    print("\n## ETAP2: WYPISYWANIE (1 PUNKT) ##")
    print(zamowienie1.__repr__())
    print(zamowienie1.__str__())


    ##################### ETAP3 #####################
    print("\n## ETAP3: OBLICZANIE CENY, PORÓWNYWANIE (2 PUNKTY) ##")
    print(f"Ceny: {Zamowienie.ceny}")
    print(f"zamowienie1:\n{zamowienie1}")
    print(f"Cena zamowienie1: {zamowienie1.oblicz_wartosc()}")

    print(f"zamowienie2:\n{zamowienie2}")
    print(f"Cena zamowienie2: {zamowienie2.oblicz_wartosc()}")

    print(f"zamowienie1 < zamowienie2: {zamowienie1 < zamowienie2}")

    ##################### ETAP4 #####################
    print("\n## ETAP4: DODAWANIE ##")
    print("## Zamowienie + Zamowienie (2 PUNKTY) ##\n")

    print("zamowienie3 = zamowienie1 + zamowienie2")
    zamowienie3 = zamowienie1 + zamowienie2
    print(f"zamowienie1:\n{zamowienie1}")
    print(f"zamowienie2:\n{zamowienie2}")
    print(f"zamowienie3:\n{zamowienie3}")

    print("\n## Zamowienie + tuple (2 PUNKTY) ##\n")
    print("zamowienie4 = zamowienie1 + (0, 3)")
    zamowienie4 = zamowienie1 + (0, 3)
    print(f"zamowienie1:\n{zamowienie1}")
    print(f"zamowienie4:\n{zamowienie4}")

    print("\nzamowienie5 = zamowienie1 + (17, 5)")
    zamowienie5 = zamowienie1 + (17, 5)
    print(f"zamowienie1:\n{zamowienie1}")
    print(f"zamowienie5:\n{zamowienie5}")
    #
    # print("\n## += (1 PUNKT) ## \n")
    # print("zamowienie1 += Zamowienie([(9, 3), (2, 5)])")
    # zamowienie1 += Zamowienie([(9, 3), (2, 5)])
    # print(f"zamowienie1:\n{zamowienie1}")
    #
    # print("\nzamowienie1 += (5, 9)")
    # zamowienie1 += (5, 9)
    # print(f"zamowienie1:\n{zamowienie1}")

if __name__=="__main__":
    main()