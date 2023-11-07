import copy
import random
random.seed(2021)

class Rectangle:
     __slots__ = ['__vertex', '__width', '__height']

     def __init__(self, punkt, szerokosc, wysokosc):
         if type(punkt[0]) != int and type(punkt[0]) != float:
             raise Exception()
         if type(punkt[1]) != int and type(punkt[1]) == float:
             raise Exception()
         if type(szerokosc) != int and type(szerokosc) != float:
             raise Exception()
         if type(wysokosc) != int and type(wysokosc) != float:
             raise Exception()
         if szerokosc < 0 or wysokosc < 0:
             raise Exception()
         self.__vertex = punkt
         self.__width = szerokosc
         self.__height = wysokosc


     def Get_area(self):
         return self.__width * self.__height

     def __str__(self):
         return f"Vertex: {self.__vertex}, width: {self.__width}, height: {self.__height}, area: {self.Get_area()}"

     def __repr__(self):
         napis = "Rectangle "
         napis += f"(__vertex = {self.__vertex},"
         napis += f" __width = {self.__width},"
         napis += f" __height = {self.__height})"
         return napis

     def __add__(self, other):
         kopia = copy.deepcopy(self)
         if type(other) == int or type(other) == float:
             kopia.__width = self.__width + other
             kopia.__height = self.__height + other
         elif type(other) == tuple:
             if len(other) != 2:
                 raise Exception()
             kopia.__width = self.__width + other[0]
             kopia.__height = self.__height + other[1]
         else:
             raise Exception()
         if kopia.__width < 0:
             kopia.__width = 0
         if kopia.__height < 0:
             kopia.__height = 0
         return kopia

     def __mul__(self, other):
         kopia = copy.deepcopy(self)
         if type(other) == int or type(other) == float:
             kopia.__width = self.__width * other
             kopia.__height = self.__height * other
         elif type(other) == tuple:
             if len(other) != 2:
                 raise Exception()
             kopia.__width = self.__width * other[0]
             kopia.__height = self.__height * other[1]
         else:
             raise Exception()
         if kopia.__width < 0:
             kopia.__width = 0
         if kopia.__height < 0:
             kopia.__height = 0
         return kopia

     def __lt__(self, other):
         if type(other) != Rectangle:
             raise Exception()
         if self.Get_area() < other.Get_area():
             return True
         elif self.Get_area() > other.Get_area():
             return False
         else:
             if self.__vertex[1] < other.__vertex[1]:
                 return True
             elif self.__vertex[1] > other.__vertex[1]:
                 return False
             else:
                 if self.__vertex[0] < other.__vertex[0]:
                     return True
                 else:
                     return False

     def __matmul__(self, other):
         if type(other) != Rectangle:
             raise Exception()
         x_d = max(self.__vertex[0], other.__vertex[0])
         y_d = max(self.__vertex[1], other.__vertex[1])
         x_g = min((self.__vertex[0] + self.__width), other.__vertex[0] + other.__width)
         y_g = min((self.__vertex[1] + self.__height), other.__vertex[1] + other.__height)
         width = x_g - x_d
         height = y_g - y_d
         return Rectangle((x_d, y_d), width, height)



def main():
    r1 = Rectangle((1, 1), 5, 10)
    r2 = Rectangle((2, 0), 7, 6)
    print(r1.__repr__())
    print(r1.__str__())
    print(r2.__repr__())
    print(r2.__str__())
    r3 = r1 + 5.5
    r4 = r1 + (-6, 2)
    print(r3)
    print(r4)
    r5 = r1 * 4.25
    r6 = r1 * (1/2, 2)
    print(r5)
    print(r6)
    lista = []
    for i in range(10):

        r6 = Rectangle((random.randint(-10, 10), random.randint(-10, 10)), random.randint(1, 10), random.randint(1, 10))
        lista.append(r6)
    for i in range(len(lista)):
        print(lista[i])
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    for i in range(len(lista)):
        print(lista[i])
    print(lista[len(lista) - 1])
    r7 = r1.__matmul__(r2)
    print(r7)





if __name__ == "__main__":
    main()