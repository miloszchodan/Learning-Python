def main():
    n = int(input("Podaj n"))
    m = int(input("Podaj m"))
    if m == 0 and n == 0:
        k = 0
    elif m >= n:
        if not m%8 == 0:
            k = m / 4 + 2
            k = int(k)
        elif m%8 == 0:
            k = m / 4 + 1
            k = int(k)
    elif m < n:
        if not n%8 == 0:
            k = n / 4 + 1
            k = int(k)
        elif n%8 == 0:
            k = n / 4
            k = int(k)






    print(f"Winda musi wykonac {k} kursow")

if __name__ == "__main__":
    main()