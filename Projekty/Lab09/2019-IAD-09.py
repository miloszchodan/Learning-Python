import csv
import math

def wczytaj_csv():
    studenci = []
    with open("studenci.csv") as f:
        for row in csv.reader(f):
            studenci.append(row)
    return studenci

def popraw(studenci):
    for i in range(0, len(studenci)):
        studenci[i][2] = int(studenci[i][2])
        for j in range(3, len(studenci[0])):
            if studenci[i][j] == '':
                licznik = 0
                suma = 0
                for l in range(3, len(studenci[0])):
                    if l == j:
                        continue
                    else:
                        if studenci[i][l] == '':
                            studenci[i][j] = 0
                            studenci[i][l] = 0
                            suma = 0
                            break
                        else:
                            licznik += 1
                            suma += float(studenci[i][l])
                studenci[i][j] = suma / licznik
            else:
                studenci[i][j] = float(studenci[i][j])
    return studenci

def wypisz(studenci):
    for i in range(0, len(studenci)):
        print("|", end = "")
        for j in range(0, len(studenci[0])):
            if type(studenci[i][j]) is not float:
                print(str(studenci[i][j]).center(12), end = "")
            else:
                studenci[i][j] = int(studenci[i][j] * 10) / 10
                print(str(studenci[i][j]).center(8), end = "")
        print("|")

def oceny(studenci):
    for i in range(0, len(studenci)):
        print("|", end="")
        suma = 0
        for j in range(3,len(studenci[0])):
            suma += studenci[i][j]
        if suma <= 50:
            ocena = 2.0
        elif suma <= 60:
            ocena = 3.0
        elif suma <= 70:
            ocena = 3.5
        elif suma <= 80:
            ocena = 4.0
        elif suma <= 90:
            ocena = 4.5
        else:
            ocena = 5.0
        print(str(studenci[i][2]).center(12), end="")
        print(str(ocena).center(8), end="")
        print("|")

def statystyki(studenci):
    for j in range(3, len(studenci[0])):
        max = 0
        min = 20
        suma = 0
        licznik = 0
        for i in range(0, len(studenci)):
            if studenci[i][j] > max:
                max = studenci[i][j]
            if studenci[i][j] < min:
                min = studenci[i][j]
            suma += studenci[i][j]
            licznik += 1
        srednia = suma / licznik
        srednia = int(srednia * 10) / 10
        print("|", end="")
        print(str(j - 2).center(12), end="")
        print(str(max).center(8), end="")
        print(str(min).center(8), end="")
        print(str(srednia).center(8), end="")
        print("|")

def main():
    studenci = wczytaj_csv()
    studenci = popraw(studenci)
    wypisz(studenci)
    oceny(studenci)
    statystyki(studenci)
if __name__ == '__main__':
    main()