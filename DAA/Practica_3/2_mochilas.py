def lee_lista(n):
    a = []
    if n >= 0:
        cadenaEntrada = input()
        for i in range(0, n):
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)

    return a


def backtracking(n, P, C, i, j, resultado, opt, opt1, opt2, cogidolista2, cogidolista1):
    if i == n:
        if j == 0:
            if resultado >= opt1:
                opt1 = resultado + opt1
                backtracking(n, P, C, 0, j + 1, 0, opt, opt1, resultado, cogidolista2, cogidolista1)
        else:
            if opt[0] < resultado + opt2:
                opt[0] = resultado + opt2


    else:
        if j == 0:
            for l in range(0, 2):
                if l == 0:
                    cogidolista1[i] = False
                    backtracking(n, P, C, i + 1, j, resultado, opt, opt1, opt2, cogidolista2, cogidolista1)
                else:
                    if cogidolista1[i]:
                        backtracking(n, P, C, i + 1, j, resultado, opt, opt1, opt2, cogidolista2, cogidolista1)
                    else:
                        resultado = P[i] + resultado
                        if resultado <= C[j]:
                            cogidolista1[i] = True
                            backtracking(n, P, C, i + 1, j, resultado, opt, opt1, opt2, cogidolista2, cogidolista1)
        else:
            for l in range(0, 2):
                if l == 0:
                    cogidolista2[i] = False
                    backtracking(n, P, C, i + 1, j, resultado, opt, opt1, opt2, cogidolista2, cogidolista1)
                else:
                    if cogidolista2[i] or cogidolista1[i]:
                        backtracking(n, P, C, i + 1, j, resultado, opt, opt1, opt2, cogidolista2, cogidolista1)
                    else:
                        resultado = P[i] + resultado
                        if resultado <= C[j]:
                            cogidolista2[i] = True
                            backtracking(n, P, C, i + 1, j, resultado, opt, opt1, opt2, cogidolista2, cogidolista1)
            if i == 0:
                for i in range(0, n):
                    cogidolista2[i] = False

    return opt[0]


n = int(input())
Pesos = lee_lista(n)
Cap = lee_lista(2)
maximo = [0]
maximo1 = 0
maximo2 = 0
cogidolista2 = [False] * n
cogidolista1 = [False] * n
backtracking(n, Pesos, Cap, 0, 0, 0, maximo, maximo1, maximo2, cogidolista2, cogidolista1)
print(int(maximo[0]))
