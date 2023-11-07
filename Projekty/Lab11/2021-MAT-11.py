import csv


def wczytaj_csv(nazwa_pliku):
    data = []
    with open(nazwa_pliku) as f:
        for row in csv.reader(f):
            data.append([float(row[i]) if i == 0 else row[i]
                                          for i in range(len(row))])
    return data

def sprawdz_poprawnosc(y):
    if y == []:
        return False
    else:
        for i in range(1, len(y)):
            if len(y[i]) != len(y[0]):
                return False
        for i in range(1,len(y)):
            for j in range(len(y[0])):
                if type(y[i][j]) != type(y[0][j]):
                    return False
        return True

def kategorie(y, i):
    lista = []
    for j in range(len(y)):
        lista.append(y[j][i])
    lista_unikat = []
    licznik = 0
    while True:
        lista_iteracyjna = []
        if lista == []:
            break
        lista_unikat.append(lista[0])
        for i in range(1, len(lista)):
            if lista[i] == lista_unikat[licznik]:
                continue
            else:
                lista_iteracyjna.append(lista[i])
        lista = lista_iteracyjna
        licznik += 1
    return lista_unikat

def grupuj(y, by):
    unikat = kategorie(y, by)
    lista = [[] for i in range(len(unikat) + 1)]
    lista[len(unikat)] = unikat
    for i in range(len(unikat)):
        for j in range(len(y)):
            if y[j][by] == unikat[i]:
                lista[i].append(y[j])
            else:
                continue
    return lista

def policz(y_grupy, f, i):
    lista = [[0] * (len(y_grupy) - 1) for j in range(2)]
    lista[0] = y_grupy[len(y_grupy) - 1]
    for k in range(len(y_grupy) - 1):
        suma = 0
        for j in range(len(y_grupy[k])):
            suma += y_grupy[k][j][i]
        srednia = suma / len(y_grupy[k])
        print(srednia)
        lista[1][k] = srednia
    return lista





def main():
    tips = wczytaj_csv("tips.csv")
    print(sprawdz_poprawnosc(tips))
    print(kategorie(tips, 2))
    grupy = grupuj(tips, 2)
    x = policz(grupy, lambda x: sum(x) / len(x), 0)
    print(x)





if __name__ == '__main__':
    main()