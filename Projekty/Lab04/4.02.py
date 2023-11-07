import math
import random



def przyblizPi(n):
    licznik = 0
    for i in range(1, n+1):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 1 <= 1:
            licznik += 1
    return 4 * licznik / n

def main():
    n = int(input("Podaj liczbę punktów n: "))
    print(przyblizPi(n))
    print(math.pi)
if __name__ == "__main__":
    main()
