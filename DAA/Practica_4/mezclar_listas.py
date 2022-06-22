def lee_lista(n):
    a = []
    if n >= 0:
        cadenaentrada = input()
        for i in range(0, n):
            elemento = int(cadenaentrada.split(" ")[i])
            a.append(elemento)

    return a


def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    else:

        a1 = merge_sort(a[0:n // 2])
        a2 = merge_sort(a[n // 2:n])
        return merge(a1, a2)


def merge(a, b):
    if not a:
        return b
    elif not b:
        return a
    else:
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])


def min_mezclar_listas(S, result, index, solucion):
    if len(S) == 0:
        for i in range(0, len(result)):
            solucion = result[i] + solucion
        return solucion
    if len(S) == 1:
        return 0
    else:
        result.append(S[0] + S[1])
        S = S[2:]
        for i in range(0, len(S)):
            if S[i] >= result[index]:
                S.insert(i, result[index])
                break
            if i == len(S) - 1:
                S.append(result[index])
        return min_mezclar_listas(S, result, index + 1, solucion)


n = int(input())
if 100 >= n > 0:
    longitud = lee_lista(n)
    longitud = merge_sort(longitud)
    resultado = []
    print(min_mezclar_listas(longitud, resultado, 0, 0))
