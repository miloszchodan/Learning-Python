def main():
    l = int(input("Podaj ilosc graczy"))
    if not l >= 2:
        print("Bledne dane")
    t = int(input("Podaj ilosc talii"))
    if not t >= 1:
        print("Bledne dane")
    print("Ile przynajmniej talii potrzeba, by wszyscy mogli zagrać w Makao?")
    talie = (l*5 + 1)/52
    if talie == int(talie):
        print(f"{int(talie)}")
    else:
        talie = int(talie+1)
        print(f"{talie}")
    print("Czy dostępna liczba talii jest wystarczająca?")
    if t*52 >= l*5 + 1:
        print("Tak")
        gracze=(t*52-1)/5
        gracze=int(gracze)
        print(f"Do rozgrywki moze sie dolaczyc {gracze-l} graczy")
    else:
        print("Nie")

if __name__ == "__main__":
    main()