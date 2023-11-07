import math
import sys


def main():
    rok = int(input("Podaj rok urodzenia"))
    if not 1900 <= rok <= 2022:
        print("Bledne dane")
        sys.exit()
    miesiac = int(input("Podaj miesiac urodzenia"))
    if not 1 <= miesiac <= 12:
        print("Bledne dane")
        sys.exit()
    dzien = int(input("Podaj dzien urodzenia"))
    if miesiac == 1 and not 1 <= dzien <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac == 3 and not 1 <= dzien <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac == 5 and not 1 <= dzien <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac == 7 and not 1 <= dzien <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac == 8 and not 1 <= dzien <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac == 10 and not 1 <= dzien <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac == 12 and not 1 <= dzien <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac == 4 and not 1 <= dzien <= 30:
        print("Bledne dane")
        sys.exit()
    if miesiac == 6 and not 1 <= dzien <= 30:
        print("Bledne dane")
        sys.exit()
    if miesiac == 9 and not 1 <= dzien <= 30:
        print("Bledne dane")
        sys.exit()
    if miesiac == 11 and not 1 <= dzien <= 30:
        print("Bledne dane")
        sys.exit()
    if miesiac == 2:
        if rok%4 == 0 and not rok%100 == 0 and not 1 <= dzien <= 29:
            print("Bledne dane")
            sys.exit()
        elif rok%400 == 0 and not 1 <= dzien <= 29:
            print("Bledne dane")
            sys.exit()
        elif not 1 <= dzien <= 28:
            print("Bledne dane")
            sys.exit()

    if miesiac == 1 or miesiac == 2:
        print("Urodziles sie w zime")
    elif miesiac == 3:
        if dzien < 21:
            print("Urodziles sie w zime")
        else:
            print("Urodziles sie w wiosne")
    elif miesiac == 4 or miesiac == 5:
        print("Urodziles sie w wiosne")
    elif miesiac == 6:
        if dzien < 22:
            print("Urodziles sie w wiosne")
        else:
            print("Urodziles sie w lato")
    elif miesiac == 7 or miesiac == 8:
        print("Urodziles sie w lato")
    elif miesiac == 9:
        if dzien < 23:
            print("Urodziles sie w lato")
        else:
            print("Urodziles sie w jesien")
    elif miesiac == 10 or miesiac == 11:
        print("Urodziles sie w jesien")
    elif miesiac == 12:
        if dzien < 22:
            print("Urodziles sie w jesien")
        else:
            print("Urodziles sie w zime")

    if miesiac == 1 or miesiac == 2:
        Y = rok - 1
    else:
        Y = rok
    if Y >= 2000:
        y = Y - 2000
        c = 20
    elif 1900 <= Y < 2000:
        y = Y - 1900
        c = 19
    else:
        y = 99
        c = 18
    if miesiac == 3:
        m = 1
    elif miesiac == 4:
        m = 2
    elif miesiac == 5:
        m = 3
    elif miesiac == 6:
        m = 4
    elif miesiac == 7:
        m = 5
    elif miesiac == 8:
        m = 6
    elif miesiac == 9:
        m = 7
    elif miesiac == 10:
        m = 8
    elif miesiac == 11:
        m = 9
    elif miesiac == 12:
        m = 10
    elif miesiac == 1:
        m = 11
    elif miesiac == 2:
        m = 12
    w = (dzien + math.floor(2.6*m-0.2) + y + math.floor(y/4) + math.floor(c/4) - 2*c) % 7
    if w < 0:
        w+=7
    if w == 0:
        print("Była to niedziela")
    elif w == 1:
        print("Był to poniedzialek")
    elif w == 2:
        print("Był to wtorek")
    elif w == 3:
        print("Była to sroda")
    elif w == 4:
        print("Był to czwartek")
    elif w == 5:
        print("Był to piatek")
    elif w == 6:
        print("Była to sobota")

    rok_1 = int(input("Podaj rok referencyjny"))
    if not 1900 <= rok_1:
        print("Bledne dane")
        sys.exit()
    miesiac_1 = int(input("Podaj miesiac referencyjny"))
    if not 1 <= miesiac_1 <= 12:
        print("Bledne dane")
        sys.exit()
    dzien_1 = int(input("Podaj dzien referencyjny"))
    if miesiac_1 == 1 and not 1 <= dzien_1 <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac_1 == 3 and not 1 <= dzien_1 <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac_1 == 5 and not 1 <= dzien_1 <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac_1 == 7 and not 1 <= dzien_1 <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac_1 == 8 and not 1 <= dzien_1 <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac_1 == 10 and not 1 <= dzien_1 <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac_1 == 12 and not 1 <= dzien_1 <= 31:
        print("Bledne dane")
        sys.exit()
    if miesiac_1 == 4 and not 1 <= dzien_1 <= 30:
        print("Bledne dane")
        sys.exit()
    if miesiac_1 == 6 and not 1 <= dzien_1 <= 30:
        print("Bledne dane")
        sys.exit()
    if miesiac_1 == 9 and not 1 <= dzien_1 <= 30:
        print("Bledne dane")
        sys.exit()
    if miesiac_1 == 11 and not 1 <= dzien_1 <= 30:
        print("Bledne dane")
        sys.exit()
    if miesiac_1 == 2:
        if rok_1 % 4 == 0 and not rok_1 % 100 == 0 and not 1 <= dzien_1 <= 29:
            print("Bledne dane")
            sys.exit()
        elif rok_1 % 400 == 0 and not 1 <= dzien_1 <= 29:
            print("Bledne dane")
            sys.exit()
        elif not 1 <= dzien_1 <= 28:
            print("Bledne dane")
            sys.exit()
    if rok_1 < rok:
        print("Data referencyjna nie moze byc wczesniejsza niz data urodzin.")
        sys.exit()
    elif rok_1 == rok:
        if miesiac_1 < miesiac:
            print("Data referencyjna nie moze byc wczesniejsza niz data urodzin.")
            sys.exit()
        elif miesiac_1 == miesiac:
            if dzien_1 < dzien:
                print("Data referencyjna nie moze byc wczesniejsza niz data urodzin.")
                sys.exit()












if __name__ == "__main__":
    main()