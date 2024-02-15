from random import *
from time import time


def gera():
    global K, lista
    lista = []

    K = randint(1, 2 * N)

    for i in range(N):
        lista.append(randint(1, N))


def algoritmo1():
    for i in range(N):
        for j in range(i, N):
            if lista[i] == lista[j]:
                continue

            if lista[i] + lista[j] == K:
                encontrado = True

    if encontrado:
        print("True")
    else:
        print("False")


def algoritmo2():
    lista.sort()

    ini = 0
    fim = N - 1

    while ini != fim and lista[ini] != lista[fim]:
        soma = lista[ini] + lista[fim]

        if soma == K:
            print("True")
            return
        if soma < K:
            ini += 1
        elif soma > K:
            fim -= 1

    print("False")


def algoritmo3():
    check = [0] * 2 * N

    for elemento in lista:
        if check[K - elemento]:
            print("True")
            return
        check[elemento] = 1

    print("False")


def main():
    global N, K, lista

    for i in range(1, 6):
        N = i * 20000
        gera()

        t1ini = time()
        algoritmo1()
        t1fim = time()

        t3ini = time()
        algoritmo3()
        t3fim = time()

        t2ini = time()
        algoritmo2()
        t2fim = time()

        print("\\/\\/\\/", N, "\\/\\/\\/")
        print(t1fim - t1ini)
        print(t2fim - t2ini)
        print(t3fim - t3ini)
        print("/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\")


if __name__ == "__main__":
    main()
