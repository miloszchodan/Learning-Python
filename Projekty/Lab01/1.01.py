def main():

    ilosc_schodow = int(input("Podaj liczbe schodow ktora pokonales"))
    if not 0 <= ilosc_schodow <= 300:
        print("Bledne dane")
    pietro = ilosc_schodow/15
    pietro = int(pietro)
    if ilosc_schodow%15==0:
        print(f"Jesteś na {pietro} pietrze")
        if pietro%2==2:
            print("Masz 0 schodkow do toalety")
        else:
            print(f"Musisz pokonać 15 schodkow w gore lub w dol do toalety")
    else:
        print(f"Jestes pomiedzy {pietro} i {pietro+1} pietrem")
        if pietro%2==0:
            print(f"Musisz pokonac {(pietro+1)*15-ilosc_schodow} schodow w dol do najblizszej toalety")
        else:
            print(f"Musisz pokonac {(pietro+1)*15-ilosc_schodow} schodow w gore do najblizszej toalety")

if __name__ == "__main__":
    main()