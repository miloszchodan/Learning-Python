def main():
    a = float(input("Podaj a"))
    b = float(input("Podaj b"))
    c = float(input("Podaj c"))
    d = float(input("Podaj d"))
    e = float(input("Podaj e"))
    f = float(input("Podaj f"))
    w = a*e - b*d
    wx = c*e - b*f
    wy = a*f - c*d
    if w == 0:
        if wx == 0 and wy == 0:
            print("Uklad nieoznaczony")
        else:
            print("Układ sprzeczny")
    else:
        x = wx/w
        y = wy/w
        print(f"Rozwiazaniem tego ukladu sa liczby {x} i {y}")
if __name__ == "__main__":
    main()