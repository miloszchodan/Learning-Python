class Sequence:
    __slots__ = ['__elements']

    def __init__(self, n, data = None):
        if type(n) != int:
            raise Exception()
        if n < 0:
            raise Exception()
        if data == None:
            self.__elements = [0] * n
        elif type(data) == list:
            if len(data) != n:
                raise Exception()
            else:
                self.__elements = data
        else:
            raise Exception()

    def Length(self):
        return len(self.__elements)

    def __repr__(self):
        napis = f"Sequence with {self.Length()} elements:\n"
        for i in range(self.Length()):
            napis += f"   {self.__elements[i]},"
        return napis

    def __getitem__(self, item):
        if type(item) != int:
            raise Exception()
        if item > len(self.__elements) - 1 or item < 0:
            raise Exception()
        return self.__elements[item]

    def __setitem__(self, key, value):
        if type(key) != int:
            raise Exception()
        if key > len(self.__elements) - 1 or key < 0:
            raise Exception()
        if type(value) != int:
            raise ValueError()
        self.__elements[key] = value

    def __add__(self, other):
        if type(other) != Sequence:
            raise Exception()
        l = max(len(self.__elements), len(other.__elements))
        lista = [0] * l
        for i in range(len(self.__elements)):
            lista[i] += self.__elements[i]
        for i in range(len(other.__elements)):
            lista[i] += other.__elements[i]
        return Sequence(l, lista)

    def Arithmetic(self):
        r = self.__elements[1] - self.__elements[0]
        for i in range(1, len(self.__elements) - 1):
            if self.__elements[i + 1] - self.__elements[i] != r:
                return False
        return True

    def Geometric(self):
        lista_zer = [0] * len(self.__elements)
        if self.__elements == lista_zer:
            return True
        else:
            if self.__elements[0] != 0:
                q = self.__elements[1] / self.__elements[0]
                for i in range(1, len(self.__elements) - 1):
                    if self.__elements[i + 1] / self.__elements[i] != q:
                        return False
                return True
            else:
                return False


def main():
    S1 = Sequence(6)
    S2 = Sequence(8, [0, 2, 4, 6, 8, 10, 12, 14])
    print(S1.Length())
    print(S2.Length())
    print(S1)
    print(S2)
    print(S2.__getitem__(3))
    print(S2.__getitem__(6))
    S1.__setitem__(5, 8)
    print(S1)
    S = Sequence(6, [1, 3, 9, 27, 81, 235])
    S3 = S1 + S
    print(S3)
    S4 = S2 + S3
    print(S4)
    print(S1.Arithmetic())
    print(S1.Geometric())
    print(S2.Arithmetic())
    print(S2.Geometric())
    print(S3.Arithmetic())
    print(S3.Geometric())
    print(S4.Arithmetic())
    print(S4.Geometric())



if __name__ == "__main__":
    main()