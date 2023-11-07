import math

def main():
    licznik = 0
    a = int(input("Podaj a"))
    b = int(input("Podaj b"))
    for i in range(a, b+1, 1):
        for j in range(2, int(math.sqrt(i)+1), 1):
            if not i % j == 0:
                licznik += 1
    print(f"W przedziale {a}, {b} jest {licznik} liczb pierwszych")



if __name__ == "__main__":
    main()