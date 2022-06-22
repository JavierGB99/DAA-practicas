def lee_lista(n):
    a = []
    if n >= 0:
        cadenaEntrada = input()
        for i in range(0, n):
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)

    return a


def imprime_lista(a):
    n = len(a)
    if n == 0:
        pass
    elif n == 1:
        print(a[0])
    else:
        print(a[0], end='')
        print(' ', end='')
        imprime_lista(a[1:])


def insertSortedList(S, elemento, acumulador):
    if len(S)-1 == acumulador:
        S[acumulador] = elemento
        imprime_lista(S)
    else:
        if S[acumulador] >= elemento:
            for i in range(len(S)-1,acumulador,-1):
                S[i]=S[i-1]
            S[acumulador]=elemento
            imprime_lista(S)
        else:
            insertSortedList(S, elemento, acumulador + 1)


tamanio = int(input())
S = lee_lista(tamanio)
elemento = float(input())
if tamanio <= 0:
    print (int(elemento))
else:
    S.append(0)
    insertSortedList(S, int(elemento), 0)
