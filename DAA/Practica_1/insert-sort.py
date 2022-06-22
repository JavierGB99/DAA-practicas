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

def insertSortedList(S, elemento, acumulador,max):
    if len(S) == 1 or len(S)-1 == acumulador:
        S[acumulador]=elemento
        return S
    else:
        if S[acumulador] >= elemento:
            for i in range(max,acumulador,-1):
                S[i]=S[i-1]
            S[acumulador]=elemento
            return S
        else:
            insertSortedList(S, elemento, acumulador + 1,max)

def recursion(S,P,tamanio,acumulador):
    if acumulador>=tamanio:
        imprime_lista(P)
    else:
        if acumulador==0 or S[acumulador]>P[acumulador-1]:
            P[acumulador]=S[acumulador]
            recursion(S,P,tamanio,acumulador+1)
        else:
            insertSortedList(P,S[acumulador],0,acumulador)
            recursion(S,P,tamanio,acumulador+1)

tamanio = int(input())
S = lee_lista(tamanio)
P=[0]*tamanio
recursion(S,P,tamanio,0)