import random

def losuj_litery(dlugosc):
    lista = [0] * dlugosc
    for i in range(0, dlugosc):
        a = random.randint(97,122)
        a = chr(a)
        lista[i] = a
    return lista

def polacz_z_zawijaniem(pierwsza, druga):
    if len(pierwsza) >= len(druga):
        n = 2 * len(pierwsza)
    else:
        n = 2 * len(druga)
    lista = [0] * n
    for i in range(0, int(n / 2)):
        lista[i] = pierwsza[i % len(pierwsza)]
    for i in range(int(n / 2), n):
        lista[i] = pierwsza[(i - int(n / 2)) % len(druga)]
    return lista

def odwroc(lista,poczatkowy,koncowy):
    nowa_lista = [0] * len(lista)
    for i in range(0,poczatkowy):
        nowa_lista[i] = lista[i]
    licznik = 0
    for i in range(poczatkowy, koncowy + 1):
        nowa_lista[i] = lista[koncowy - licznik]
        licznik += 1
    for i in range(koncowy + 1, len(lista)):
        nowa_lista[i] = lista[i]
    return nowa_lista

def przesun_w_lewo(lista, n):
    nowa_lista = [0] * len(lista)
    for i in range(0, len(lista) - n):
        nowa_lista[i] = lista[i + n]
    for i in range(len(lista) - n, len(lista)):
        nowa_lista[i] = lista[i - n - 1]
    return nowa_lista

def mod_26(tab):
    for i in range(0, len(tab)):
        if i == 0:
            a = 0
            b = tab[0]
            c = tab[1]
        elif i == len(tab) - 1:
            a = tab[len(tab) - 2]
            b = tab[len(tab) - 1]
            c = 0
        else:
            a = tab[i - 1]
            b = tab[i]
            c = tab[i + 1]
        tab[i] = chr((ord(a) + ord(b) + ord(c)) % 26)
    return tab
def main():
    random.seed(2014)
    dlugosc_1 = int(input("Podaj dlugosc: "))
    if not 5 <= dlugosc_1 <= 15:
        raise ValueError
    print(f"losuj liter: {dlugosc_1}")
    lista_1 = losuj_litery(dlugosc_1)
    print(lista_1)
    dlugosc_2 = int(input("Podaj dlugosc: "))
    if not 5 <= dlugosc_2 <= 15:
        raise ValueError
    print(f"losuj liter: {dlugosc_2}")
    lista_2 = losuj_litery(dlugosc_2)
    print(lista_2)
    print("Polacz z zawijaniem")
    polacz = polacz_z_zawijaniem(lista_1, lista_2)
    print(polacz)
    a = int(input("a: "))
    b = int(input("b: "))
    print(f"odwroc pomiedzy {a} i {b}")
    odwroc_pomiedzy = odwroc(lista_2,a,b)
    print(polacz)
    print(odwroc_pomiedzy)
    c = int(input("c: "))
    przesun = przesun_w_lewo(lista_1, c)
    print(lista_1)
    print(przesun)
    mod = mod_26(['a','b','c','d'])
    print(['a','b','c','d'])
    print(mod)






if __name__ == "__main__":
    main()