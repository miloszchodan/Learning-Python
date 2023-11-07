import random
import math
random.seed(1354)

def rzucaj(n):
    suma = 0
    if n == 1:
        a = random.randint(1, 6)
        suma = suma + a
        return suma, a
    if n == 2:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        suma = suma + a + b
        return suma, a, b
    if n == 3:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 6)
        suma = suma + a + b + c
        return suma, a, b, c


def sprawdz_bonus(suma):
    licznik = 0
    for i in range(2, suma):
        if suma % i == 0:
            licznik += 1
        else:
            continue
    return licznik

def main():
    wygrywajaca = random.randint(10, 50)
    output_file = open("2020-MAT-05.txt", "w")
    output_file.write(f"Wygrywajaca: {wygrywajaca}\n")
    licznik_1 = 0
    licznik_2 = 0
    while True:
        print(f"Liczba wygrywajaca: {wygrywajaca}")
        print(f"Suma gracza 1: {licznik_1}")
        print(f"Suma gracza 2: {licznik_2}")
        print("Ruch gracza 1")
        output_file.write("Gracz 1 ")
        n = int(input("Iloma koscmi chcesz rzucic? "))
        output_file.write(f"Liczba kosci: {n}")
        output_file.write(" ")
        if n < 1 or n > 3:
            raise ValueError
        output_file.write("Wyrzucone: ")
        if n == 1:
            suma, a = rzucaj(n)
            output_file.write(str(a))
            output_file.write(" ")
        elif n == 2:
            suma, a, b = rzucaj(n)
            output_file.write(str(a))
            output_file.write(" ")
            output_file.write(str(b))
            output_file.write(" ")
        elif n == 3:
            suma, a, b, c = rzucaj(n)
            output_file.write(str(a))
            output_file.write(" ")
            output_file.write(str(b))
            output_file.write(" ")
            output_file.write(str(c))
            output_file.write(" ")
        licznik_1 += suma
        bonus = sprawdz_bonus(suma)
        output_file.write(f"Bonus: {bonus} ")
        print(f"Bonus: {bonus}")
        licznik_1 += bonus
        output_file.write(f"Suma: {licznik_1}\n")
        print(f"Liczba wygrywajaca: {wygrywajaca}")
        print(f"Suma gracza 1: {licznik_1}")
        print(f"Suma gracza 2: {licznik_2}")
        print("Ruch gracza 2")
        output_file.write("Gracz 2 ")
        n = int(input("Iloma koscmi chcesz rzucic? "))
        if not 1 <= n <= 3:
            raise ValueError
        output_file.write(f"Liczba kosci: {n}")
        output_file.write(" ")
        output_file.write("Wyrzucone: ")
        if n == 1:
            suma, a = rzucaj(n)
            output_file.write(str(a))
            output_file.write(" ")
        elif n == 2:
            suma, a, b = rzucaj(n)
            output_file.write(str(a))
            output_file.write(" ")
            output_file.write(str(b))
            output_file.write(" ")
        elif n == 3:
            suma, a, b, c = rzucaj(n)
            output_file.write(str(a))
            output_file.write(" ")
            output_file.write(str(b))
            output_file.write(" ")
            output_file.write(str(c))
            output_file.write(" ")
        licznik_2 += suma
        bonus = sprawdz_bonus(suma)
        output_file.write(f"Bonus: {bonus} ")
        print(f"Bonus: {bonus}")
        licznik_2 += bonus
        output_file.write(f"Suma: {licznik_2}\n")
        if wygrywajaca <= licznik_1 or wygrywajaca <= licznik_2:
            break
    print(f"Liczba wygrywajaca: {wygrywajaca}")
    print(f"Suma gracza 1: {licznik_1}")
    print(f"Suma gracza 2: {licznik_2}")
    if math.fabs(licznik_1 - wygrywajaca) < math.fabs(licznik_2 - wygrywajaca):
        print("Wygral gracz 1")
        output_file.write("Wygral gracz 1")
    elif math.fabs(licznik_1 - wygrywajaca) == math.fabs(licznik_2 - wygrywajaca):
        print("Remis")
        output_file.write("Remis")
    elif math.fabs(licznik_1 - wygrywajaca) > math.fabs(licznik_2 - wygrywajaca):
        print("Wygral gracz 2")
        output_file.write("Wygral gracz 2")
    output_file.close()

if __name__ == "__main__":
    main()