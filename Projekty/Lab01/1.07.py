import sys


def main():
    odleglosc = float(input("Podaj odleglosc od domu"))
    hajs = float(input("Podaj ilosc gotowki jaka masz"))
    if hajs < 0 or odleglosc < 0:
        print("Bledne dane")
        sys.exit()
    if hajs < 10:
        print("Nie stac Cie na wejscie")
    if hajs <= 60:
        zasieg = (hajs - 10)/2.5
    elif hajs > 60:
        zasieg = (hajs - 60)/5 + 20
    print(f"Zasieg to {zasieg}")
    if zasieg >= odleglosc:
        print("Uda ci sie dojechac")
    else:
        print("Nie uda ci sie dojechac")






if __name__ == "__main__":
    main()