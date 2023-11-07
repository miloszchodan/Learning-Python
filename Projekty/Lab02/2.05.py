def main():
    k = int(input("Podaj k"))
    if not k > 0:
        raise Exception("Błąd")
    licznik = 1
    x0 = 1
    while True:
        x = x0
        print("Nowy ciąg")
        print(x0)
        while x != 1:
            licznik +=1
            if x % 2 == 0:
                x = x / 2
            else:
                x = 3 * x + 1
                print(x)
        if licznik < k:
            licznik = 1
            x0 += 1
        else:
            break
    print(f"Pierwszy wyraz ciagu ma wartosc {x0} i ma {licznik} wyrazow")


if __name__ == "__main__":
    main()