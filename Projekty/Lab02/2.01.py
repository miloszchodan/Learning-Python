import sys
import math


def main():
    cukierki = 100
    while True:
        print(f"Pozostalo {cukierki} cukierkow")
        a = math.nan
        b = math.nan
        a = int(input("Ile cukierków bierze pierwszy gracz?"))
        if a > cukierki or a > b:
            print("Blad!")
            sys.exit()
        cukierki -= a
        if cukierki == 0:
            print("Wygral gracz pierwszy")
            sys.exit()
        print(f"Pozostalo {cukierki} cukierkow")
        b = int(input("Ile cukierkow bierze drugi gracz?"))
        if b > cukierki or b > a:
            print("Blad!")
            sys.exit()
        cukierki -= b
        if cukierki == 0:
            print("Wygral gracz drugi")
            sys.exit()
if __name__ == "__main__":
    main()