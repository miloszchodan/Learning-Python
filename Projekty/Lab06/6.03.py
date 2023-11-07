import math

def pierwsze(k):
    lista = [True] * (k - 1)
    for i in range(2, int(math.sqrt(k) + 1), 1):
        if lista[i - 2] == True:
            for j in range(i, k + 1):
                if j % i == 0:
                    lista[j - 2] = False
                lista[i - 2] = True
    return lista

def main():
    k = int(input("Podaj k: "))
    p = pierwsze(k)
    for i in range(1, k + 1):
        if (i - 1) % 10 == 0:
            print("")
        if i == 1:
            print(" ", end="")
        elif p[i - 2] == True:
            print("o", end="")
        elif p[i - 2] == False:
            print(".", end="")

if __name__ == "__main__":
    main()








