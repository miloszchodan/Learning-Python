import copy


def wypisz_os(x_max, krok):
    print('0', end='')
    i = krok
    while i <= x_max:
        print(f'{i:.>{krok}d}', end='')
        i += krok
    print('.' * (x_max - i))




def wypisz_przedzialy(przedzialy, x_max, krok):
    assert isinstance(przedzialy, list), "Podany obiekt nie jest listą."
    wypisz_os(x_max, krok)
    for i in range(len(przedzialy)):
        if not (isinstance(przedzialy[i], tuple) or isinstance(przedzialy[i], list)):
            print(f'Przedział {i} nie jest listą/krotką.')
        elif len(przedzialy[i]) != 2:
            print(f'Przedział {i} nie ma długości 2.')
        elif not (0 <= przedzialy[i][0] < przedzialy[i][1] <= x_max):
            print(f'Nieprawidłowe końce przedziału: "{przedzialy[i]}"')
        else:
            a, b = przedzialy[i]
            print(' ' * a + '#' * (b - a + 1) + ' ' * (x_max - b), end='')
            print(f' [{a:2d}, {b:2d}], dlugosc={b - a + 1}')

def skurcz(przedzialy, k, d):
    przedzialy_1 = copy.deepcopy(przedzialy)
    lista = []
    for i in range(len(przedzialy_1)):
        a, b = przedzialy_1[i]
        b -= k
        a += k
        if b - a + 1 < d:
            continue
        else:
            c = a, b
            lista.append(c)
    return lista

def odleglosc(p1, p2):
    a, b = p1
    c, d = p2
    if c - b < 0:
        return 0
    else:
        return c - b

def znajdz_bliskie(przedzialy, k):
    lista = []
    for i in range(len(przedzialy)):
        for j in range(i + 1, len(przedzialy)):
            p1 = przedzialy[i]
            p2 = przedzialy[j]
            d = odleglosc(p1, p2)
            krotka = p1, p2, d
            if 0 < d <= k:
                lista.append(krotka)
            else:
                continue
    return lista





def main():
    PRZYKLADOWE_DANE = [(1, 10), (12, 30), (15, 25), (26, 29), (7, 21), (32, 38)]
    N = 40
    krok = 5
    k = 2
    d = 3
    wypisz_przedzialy(PRZYKLADOWE_DANE, N, krok)
    skrocone = skurcz(PRZYKLADOWE_DANE, k, d)
    wypisz_przedzialy(skrocone, N, krok)
    print(odleglosc((5, 10), (13, 15)))
    print(odleglosc((5, 10), (11, 15)))
    print(odleglosc((5, 10), (10, 15)))
    print(odleglosc((5, 10), (7, 15)))
    lista = znajdz_bliskie(PRZYKLADOWE_DANE, d)
    print(lista)



if __name__ == '__main__':
    main()