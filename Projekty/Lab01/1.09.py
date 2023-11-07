def main():
    pizza = int(input("Podaj ilosc pizz"))
    napoj = int(input("Podaj ilosc napoju"))
    if  pizza < 1 or napoj < 1:
        koszt = pizza * 19.99 + napoj * 6.99 + 5
    else:
        if pizza >= napoj:
            koszt = napoj * 25.99 + (pizza - napoj) * 19.99
        elif napoj > pizza:
            koszt = pizza * 25.99 + (napoj - pizza) * 6.99
    print(f"Zamowienie bedzie kosztowac {koszt}")



if __name__ == "__main__":
    main()