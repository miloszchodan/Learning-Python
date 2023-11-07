def main():
    s = int(input("Podaj wartosc ziarna s"))
    n = int(input("Podaj ile wartosci wygenerowac"))
    m = 2 ** 31 - 1
    a = 1103515245
    c = 12345
    liczby = open("../../AppData/Roaming/JetBrains/PyCharmCE2022.2/scratches/liczby.txt", "w")
    for i in range(1, n+1):
        s = (a * s + c) % m
        liczby.write(str(s / m))
        liczby.write(f"\n")
    liczby.close()
if __name__ == "__main__":
    main()
