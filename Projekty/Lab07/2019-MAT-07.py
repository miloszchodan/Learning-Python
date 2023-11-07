def liczby(a,b,c,d,n):
    lista = [0] * n
    lista_1 = [a]
    lista_2 = [b,c,d]
    lista = lista_2
    for i in range(2, n):
        nowa_lista = funkcja_pomocnicza(lista, i)
        lista = nowa_lista
    return lista

def funkcja_pomocnicza(lista_n, n):
    lista_n_1 = [0] * (2 * n + 1)
    if n == 2:
        lista_n_1[0] = lista_n[0]
        lista_n_1[1] = lista_n[0] + lista_n[1]
        lista_n_1[2] = lista_n[0] + lista_n[1] + lista_n[2]
        lista_n_1[3] = lista_n[1] + lista_n[2]
        lista_n_1[4] = lista_n[2]
    elif n == 3:
        lista_n_1[0] = lista_n[0]
        lista_n_1[1] = lista_n[0] + lista_n[1]
        lista_n_1[2] = lista_n[0] + lista_n[1] + lista_n[2]
        lista_n_1[3] = lista_n[1] + lista_n[2] + lista_n[3]
        lista_n_1[4] = lista_n[2] + lista_n[3] + lista_n[4]
        lista_n_1[5] = lista_n[3] + lista_n[4]
        lista_n_1[6] = lista_n[4]
    else:
        lista_n_1[0] = lista_n[0]
        lista_n_1[1] = lista_n[0] + lista_n[1]
        for i in range(2,2 * n - 1):
            lista_n_1[i] = lista_n[i - 1] + lista_n[i] + lista_n[i + 1]
        lista_n_1[2 * n - 1] = lista_n[2 * n - 2] + lista_n[2 * n - 3]
        lista_n_1[2 * n] = lista_n[2 * n - 2]
        return lista_n_1




def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    n = int(input())
    if n < 3:
        raise ValueError
    lista = liczby(a,b,c,d,n)
    print(f"TrinomialPlusInt({a}, {b}, {c}, {d}, {n})=={lista}")

if __name__ == "__main__":
    main()