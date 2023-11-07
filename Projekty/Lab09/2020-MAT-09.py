import random


def wypisz_macierz(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if type(matrix[row][column]) is float:
                print(f'{matrix[row][column]:6.2}', end=" ")
            else:
                print(f'{matrix[row][column]:6}', end=" ")
        print()
    print()

def losuj_macierz(wiersze, kolumny, a, b):
    return [[random.randint(a, b) for j in range(kolumny)] for i in range(wiersze)]

def losuj_wektor(n, a, b):
    return [random.randint(a, b) for j in range(n)]

def mnoz_macierz_wektor(A, b):
    if len(b) != len(A[0]):
        raise Exception
    c = [0] * len(A)
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            c[i] += A[i][j] * b[j]
    return c

def macierz_vandermonde(alfa, n):
    M = [[0] * n for i in range(0, len(alfa))]
    for i in range(0, len(alfa)):
        M[i][0] = 1
        for j in range(1, n):
            M[i][j] = M[i][j - 1] * alfa[i]
    return M

def czy_macierz_permutacji(macierz):
    if len(macierz) != len(macierz[0]):
        return False
    for i in range(0, len(macierz)):
        licznik = 0
        for j in range(0, len(macierz[0])):
            if not macierz[i][j] == 1 and not macierz[i][j] == 0:
                return False
            if macierz[i][j] == 1:
                licznik +=1
            if licznik > 1:
                return False
    for i in range(0, len(macierz[0])):
        licznik = 0
        for j in range(0, len(macierz)):
            if not macierz[i][j] == 1 and not macierz[i][j] == 0:
                return False
            if macierz[i][j] == 1:
                licznik += 1
            if licznik > 1:
                return False

    return True



def main():
    random.seed(123)
    wiersze = 3
    kolumny = 4
    n = 4
    a = 0
    b = 4
    alfa = [1, 2, 3, 5, 7]
    A = losuj_macierz(wiersze, kolumny, a, b)
    wektor = losuj_wektor(n, a, b)
    iloczyn = mnoz_macierz_wektor(A, wektor)
    wypisz_macierz(A)
    print(wektor)
    print(iloczyn)
    M = macierz_vandermonde(alfa, n)
    wypisz_macierz(M)
    macierz_permutacji = [[0] * 3 for i in range(0, 3)]
    macierz_permutacji[0][0] = macierz_permutacji[1][0] = 0
    macierz_permutacji[2][0] = 1
    macierz_permutacji[1][1] = macierz_permutacji[2][1] = 0
    macierz_permutacji[0][1] = 1
    macierz_permutacji[0][2] = macierz_permutacji[2][2] = 0
    macierz_permutacji[1][2] = 1
    wypisz_macierz(macierz_permutacji)
    print(czy_macierz_permutacji(macierz_permutacji))
if __name__ == '__main__':
    main()