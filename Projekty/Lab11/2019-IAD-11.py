import copy


def wczytaj():
    lista = []
    with open('../../../AppData/Roaming/JetBrains/PyCharmCE2022.2/scratches/dane.txt', 'r') as f:
        for line in f:
            element = int(line)
            if element >= 0:
                lista.append(element)
    return lista

def sprawdz_poprawnosc(y):
    if y == []:
        return False
    else:
        for i in range(len(y)):
            if y[i] < 0:
                return False
            elif y[i] != int(y[i]):
                return False
    return True

def podziel(y):
    lista = [[y[0]]]
    licznik = 0
    for i in range(1, len(y)):
        if y[i] > y[i - 1]:
            lista[licznik].append(y[i])
        else:
            lista.append([])
            licznik += 1
            lista[licznik].append(y[i])
    return lista

def wypisz(x):
    for i in range(len(x)):
        print(f"x[ {i} ]:    ", end="")
        licznik = 0
        while True:
            if licznik == len(x[i]):
                break
            else:
                print(f"{x[i][licznik]}     ", end="")
                licznik += 1
        print("")

def zlacz_posortowane(x):
    y = []
    for i in range(len(x)):
        licznik = 0
        while True:
            if licznik == len(x[i]):
                break
            else:
                y.append(x[i][licznik])
                licznik += 1
    for i in range(len(y)):
        for j in range(len(y) - i - 1):
            if y[j] > y[j + 1]:
                y[j], y[j + 1] = y[j + 1], y[j]
    return y

def main():
    y = wczytaj()
    x = podziel(y)
    wypisz(x)
    z = copy.deepcopy(x)
    print(zlacz_posortowane(z))

if __name__ == '__main__':
    main()