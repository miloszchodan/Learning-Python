def main():
    waga = float(input("Podawaj wage (w kg)"))
    if waga <= 0:
        print("Bledne dane")
    wzrost = float(input("Podaj wzrost (w cm)"))
    if wzrost <= 0:
        print("Bledne dane")
    BMI = waga*10000/(wzrost**2)
    if BMI <= 18.5:
        print("Niedowaga")
    elif 18.5 < BMI <= 25:
        print("Waga prawidłowa")
    elif 25 < BMI <= 30:
        print("Nadwaga")
    else:
        print("Otylosc")


if __name__ == "__main__":
    main()