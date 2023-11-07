def podajA():
    n = int(input("Podaj rozmiar zbioru A: "))
    lista = [0] * n
    print("Podaj elementy zbioru A:")
    for i in range(0, n):
        lista[i] = int(input(f"Podaj ilość {i}: "))
    if lista[n - 1] == 0:
        raise ValueError
    return lista

def podajB():
    n = int(input("Podaj rozmiar zbioru B: "))
    lista = [0] * n
    print("Podaj elementy zbioru B:")
    for i in range(0, n):
        lista[i] = int(input(f"Podaj ilość {i}: "))
    if lista[n - 1] == 0:
        raise ValueError
    return lista


def wypisz(lista):
    suma = 0
    for i in range(0, len(lista)):
        suma += lista[i]
    multizbior = [0] * suma
    licznik = 0
    for i in range(0, len(lista)):
        if lista[i] == 0:
            continue
        else:
            for j in range(1, lista[i] + 1):
                multizbior[licznik] = i
                licznik += 1
    return multizbior

def dodaj(zbior, element):
    suma = [0] * (element + 1)
    if len(zbior) - 1 >= element:
        zbior[element] += 1
        suma = zbior
    else:
        for i in range(0,len(zbior)):
            suma[i] = zbior[i]
        for i in range(len(zbior),element):
            if i == element - 1:
                suma[i] = 1
            else:
                suma[i] = 0
    multizbior = wypisz(suma)
    return multizbior

def przeciecie(zbiorA, zbiorB):
    if len(zbiorA) >= len(zbiorB):
        n = len(zbiorB)
    else:
        n = len(zbiorA)
    lista = [0] * n
    for i in range(0, n):
        lista[i] = min(zbiorA[i], zbiorB[i])
    multizbior = wypisz(lista)
    return multizbior

def roznica(zbiorA, zbiorB):
    lista = [0] * len(zbiorA)
    for i in range(0, len(zbiorA)):
        if zbiorA[i] - zbiorB[i] <= 0:
            lista[i] = 0
        else:
            lista[i] = zbiorA[i] - zbiorB[i]
    while True:
        if lista[len(lista) - 1] == 0:
            nowa_lista = [0] * (len(lista) - 1)
            for i in range(0, len(lista) - 1):
                nowa_lista[i] = lista[i]
            lista = nowa_lista
        else:
            break
    multizbior = wypisz(lista)
    return multizbior

def main():
    listaA = podajA()
    print(f"Podany zbior to: {wypisz(listaA)}")
    elementA = int(input("Podaj nowy element zbioru A: "))
    print(f"Zbior A po dodaniu elementu; {dodaj(listaA,elementA)}")
    listaB = podajB()
    print(f"Roznica zbiorow to {roznica(listaA, listaB)}")
    print(f"Przciecie podanych zbiorw to {przeciecie(listaA, listaB)}")





if __name__ == "__main__":
    main()





