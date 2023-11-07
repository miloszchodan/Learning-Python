def main():
    masa = float(input("Podaj wage (w kg)"))
    if masa <= 0:
        print("Bledne dane")
    objetosc = float(input("Podaj ilosc spozytego alkoholu (w ml)"))
    if objetosc <= 0:
        print("Bledne dane")
    moc = float(input("Podaj procentowa zawartosc alkoholu w trunku (liczby calkowite)"))
    if not 0 <= moc <= 100:
        print("Bledne dane")
    plec = str(input("Podaj plec"))
    if not plec == "mezczyzna" or plec == "kobieta":
        print("Bledne dane")
    if plec == "mezczyzna":
        k = 0.7
    else:
        k = 0.6
    promile=(objetosc*moc/1.25/100)/(k/masa)
    if promile <= 0.2:
        print("Trzezwy")
    elif 0.2 < promile <= 5:
        print("Niezdolny do prowadzenia pojazdow mechanicznych")
    else:
        print("Stan zagrozenia zycia")



if __name__ == "__main__":
    main()