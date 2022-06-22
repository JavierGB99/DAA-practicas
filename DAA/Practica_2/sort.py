def odd(a):
    if a % 2 != 0:
        return True


def even(a):
    if a % 2 == 0:
        return True


def lee_lista(n):
    a = []
    if n >= 0:
        cadenaentrada = input()
        for i in range(0, n):
            elemento = int(cadenaentrada.split(" ")[i])
            a.append(elemento)

    return a


def imprime_lista(a):
    n = len(a)
    if n == 0:
        pass
    if n == 1:
        print(a[0])
    else:
        for i in range(0, n):
            print(a[i], end='')
            print(' ', end='')


def merge_sort(S, inf, sup):
    n = len(S)
    if n <= 1:
        return S
    elif n == 2:
        if even(S[0]) and odd(S[1]):
            S[0], S[1] = S[1], S[0]
            return S
        elif odd(S[0]) and even(S[1]):
            S[0], S[1] = S[0], S[1]
            return S
        else:
            if S[0] > S[1]:
                S[0], S[1] = S[1], S[0]
                return S
            else:
                return S
    else:
        mitad = n // 2
        izq = merge_sort(S[0:n // 2], 0, mitad)
        dcha = merge_sort(S[n // 2:n], inf + mitad, sup - 1)
        return mezclar(izq, dcha)


def mezclar(izq, dcha):
    s = []
    num_impares_izq = 0
    num_impares_dcha = 0
    i = 0
    z = len(izq)
    j = 0
    l = len(dcha)
    while (i < z and odd(izq[i])) or (j < l and odd(dcha[j])):

        if i >= z:
            s.append(dcha[j])
            j += 1
            num_impares_dcha += 1

        elif even(izq[i]):
            s.append(dcha[j])
            j += 1
            num_impares_dcha += 1

        elif j >= l:
            s.append(izq[i])
            i += 1
            num_impares_izq += 1

        elif even(dcha[j]):
            s.append(izq[i])
            i += 1
            num_impares_izq += 1
        elif izq[i] < dcha[j]:
            s.append(izq[i])
            i += 1
            num_impares_izq += 1
        else:
            s.append(dcha[j])
            j += 1
            num_impares_dcha += 1

    i = 0 + num_impares_izq
    j = 0 + num_impares_dcha
    while (i < z) or (j < l):

        if i >= z:
            s.append(dcha[j])
            j += 1

        elif j >= l:
            s.append(izq[i])
            i += 1

        elif izq[i] < dcha[j]:
            s.append(izq[i])
            i += 1
        else:
            s.append(dcha[j])
            j += 1

    return s


# 4 -5 6 1 8 13 0 -2 2 4 3 1 7
n = int(input())
S = lee_lista(n)
if n > 1:
    imprime_lista(merge_sort(S, 0, n - 1))
else:
    imprime_lista(S)
