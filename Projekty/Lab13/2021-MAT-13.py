import copy
import math
import random

class Punkt:
    __slots__ = ['wspolrzedne', 'n']

    def __init__(self, n = 0):
        if type(n) != int:
            raise Exception()
        if n < 0:
            self.n = 0
        else:
            self.n = n
        self.wspolrzedne = [0.0] * n

    def __repr__(self):
        return f"Punkt(n={self.n}, wspolrzedne={self.wspolrzedne})"

    def __setitem__(self, indeks, wartosc):
        if indeks > len(self.wspolrzedne) or type(indeks) != int or indeks < 0:
            raise Exception()
        self.wspolrzedne[indeks] = float(wartosc)

    def __getitem__(self, item):
        return self.wspolrzedne[item]

    def  __lt__(self, other):
        if type(other) != Punkt:
            raise Exception()
        elif self.n != other.n:
            raise Exception()
        else:
            suma_s = 0
            suma_o = 0
            for i in range(len(self.wspolrzedne)):
                suma_s += (self.wspolrzedne[i]) ** 2
                suma_o += (other.wspolrzedne[i]) ** 2
            if suma_s < suma_o:
                return True
            else:
                return False

    def __gt__(self, other):
        if type(other) != Punkt:
            raise Exception()
        elif self.n != other.n:
            raise Exception()
        else:
            suma_s = 0
            suma_o = 0
            for i in range(len(self.wspolrzedne)):
                suma_s += (self.wspolrzedne[i]) ** 2
                suma_o += (other.wspolrzedne[i]) ** 2
            if suma_s > suma_o:
                return True
            else:
                return False

    def __eq__(self, other):
        if type(other) != Punkt:
            raise Exception()
        elif self.n != other.n:
            raise Exception()
        else:
            suma_s = 0
            suma_o = 0
            for i in range(len(self.wspolrzedne)):
                suma_s += (self.wspolrzedne[i]) ** 2
                suma_o += (other.wspolrzedne[i]) ** 2
            if suma_s == suma_o:
                return True
            else:
                return False





    def ustaw(self, parametr):
        lista = []
        if type(parametr) != int and type(parametr) != list:
            raise Exception()
        if type(parametr) == list:
            if len(parametr) != len(self.wspolrzedne):
                raise Exception()
            for i in range(len(self.wspolrzedne)):
                lista.append(float(parametr[i]))
        else:
            for i in range(len(self.wspolrzedne)):
                lista.append((float(parametr)))
        self.wspolrzedne = lista

    def odleglosc(self, other):
        if type(other) != Punkt:
            raise Exception()
        if len(self.wspolrzedne) != len(other.wspolrzedne):
            return -1
        else:
            suma = 0
            for i in range(len(self.wspolrzedne)):
                suma += (self.wspolrzedne[i] - other.wspolrzedne[i]) ** 2
            suma = math.sqrt(suma)
            return suma

    def przesun(self, other):
        if type(other) != int and type(other) != list:
            raise Exception()
        elif type(other) == int:
            for i in range(len(self.wspolrzedne)):
                self.wspolrzedne[i] += other
        else:
            if len(self.wspolrzedne) != len(other):
                raise Exception()
            else:
                for i in range(len(self.wspolrzedne)):
                    self.wspolrzedne[i] += other[i]

    def odbij(self, other):
        if type(other) != Punkt:
            raise Exception()
        elif len(self.wspolrzedne) != len(other.wspolrzedne):
            return False
        else:
            for i in range(len(self.wspolrzedne)):
                self.wspolrzedne[i] = 2 * other.wspolrzedne[i] - self.wspolrzedne[i]
            return True


def main():

    print("---------------- ETAP 1 ----------------")
    P0 = Punkt(-4)
    P1 = Punkt()
    P2 = Punkt(3)
    P3 = Punkt(3)
    print(P0)
    print(P1)
    print(P2)
    print(P3)

    print("---------------- ETAP 2 ----------------")
    P2.ustaw([1, 2.0, 3])
    P3.ustaw(4)
    print(P2)
    print(P3)

    P2[2] = 7
    P3[0] = 2.0
    print(P2)
    print(P3)
    print(f"Druga wspolrzedna punktu P2 wynosi {P2[2]}")
    print(f"Zerowa wspolrzedna punktu P3 wynosi {P3[0]}")


    print("---------------- ETAP 3 ----------------")
    print(f"Odleglosc pomiedzy P2 i P3 wynosi {P2.odleglosc(P3)} \t (powinno być 3.7416573867739413)")
    print(f"Odleglosc pomiedzy P1 i P2 wynosi {P1.odleglosc(P2)} \t (powinno być -1)")

    print(f"Punkt P2: {P2}")
    P2.przesun([1, 2, 3.0])
    print(f"Punkt P2 po przesunieciu o [1, 2, 3.0]: {P2}")
    P2.przesun(-1)
    print(f"Punkt P2 po przesunieciu o -1: {P2}")

    print(f"Odbicie P2 względem [0, 0, 0]: {P2.odbij(Punkt(3))}")
    print(f"Punkt P2 po odbiciu: {P2}")

    print(f"Odbicie P2 względem P3: {P2.odbij(P3)}")
    print(f"Punkt P2 po odbiciu: {P2}")

    print(f"Odbicie P2 względem [0, 0]: {P2.odbij(Punkt(2))}")
    print(f"Punkt P2 po odbiciu: {P2}")


    print("---------------- ETAP 4 ----------------")
    print(f"P0: {P0}")
    print(f"P1: {P1}")
    print(f"P0 < P1: {P0 < P1}, powinno być False")
    print(f"P0 > P1: {P0 > P1}, powinno być False")
    print(f"P0 == P1: {P0 == P1}, powinno być True")

    print(f"P2: {P2}")
    print(f"P3: {P3}")
    print(f"P2 < P3: {P2 < P3}, powinno być False")
    print(f"P2 > P3: {P2 > P3}, powinno być True")
    print(f"P2 == P3: {P2 == P3}, powinno być False")

    print("---------------- ETAP 5 ----------------")
    random.seed(2022)
    lista = []
    for i in range(1000):
        P5 = Punkt(3)
        P5.ustaw([random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)])
        lista.append(P5)
    min = lista[0]
    max = lista[0]
    for i in range(1000):
        if lista[i] > max:
            max = lista[i]
        if lista[i] < min:
            min = lista[i]
    P6 = Punkt(3)
    P6.ustaw([100, 100, 100])
    print(f"Punkt najblizszy punktowi {P6.wspolrzedne}:")
    print(max)
    print(P6.odleglosc(max))
    print(f"Punkt najdalszy punktowi {P6.wspolrzedne}:")
    print(min)
    print(P6.odleglosc(min))

    print("---------------- Udało się!:) ----------------")

if __name__ == "__main__":
    main()