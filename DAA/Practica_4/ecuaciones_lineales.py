import math


def lee_lista(n):
    a = []
    if n >= 0:
        cadenaentrada = input()
        for i in range(0, n):
            elemento = int(cadenaentrada.split(" ")[i])
            a.append(elemento)

    return a


def lee_lista_flotantes(n):
    a = []
    if n >= 0:
        cadenaentrada = input()
        for i in range(0, n):
            elemento = float(cadenaentrada.split(" ")[i])
            a.append(elemento)

    return a


def lee_lista2D(n, m):
    a = [[0 for j in range(m)] for i in range(n)]
    if n >= 0:
        for i in range(0, n):
            cadenaentrada = input()
            for j in range(0, m):
                elemento = int(cadenaentrada.split(" ")[j])
                a[i][j] = elemento

    return a


def imprime_lista(a):
    n = len(a)
    if n == 0:
        pass
    if n == 1:
        print(format(a[0], '.4f'))
    else:
        for i in range(0, n):
            print(format(a[i], '.4f'), end='')
            print(' ', end='')


def traspuesta(A):
    a = [[0 for j in range(len(A))] for i in range(len(A[0]))]
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            elemento = A[i][j]
            a[j][i] = elemento
    return a


def multiplicar_2DA_int(A, n):
    a = [[0 for j in range(len(A[0]))] for i in range(len(A))]
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            a[i][j] = A[i][j] * n
    return a


def multiplicar_A_B(A, B):
    a = [[0 for j in range(len(A))] for i in range(len(B[0]))]
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            for k in range(0, len(A[0])):
                a[i][j] = A[i][k] * B[k][j] + a[i][j]
    return a


def multiplicar_2DA_x(A, x):
    a = [0] * len(A)
    for i in range(0, len(a)):
        for j in range(0, len(A[0])):
            a[i] = A[i][j] * x[j] + a[i]
    return a


def multiplicar_gradiente_alpha(A, alpha):
    a = [0] * len(A)
    for i in range(0, len(a)):
        a[i] = A[i] * alpha
    return a


def restar(A, B):
    a = [0] * len(A)
    for i in range(0, len(a)):
        a[i] = A[i] - B[i]
    return a


def calcular_gradiente(A2T_A, A2T_b, x):
    A2T_A_x = multiplicar_2DA_x(A2T_A, x)
    gradiente = restar(A2T_A_x, A2T_b)
    return gradiente


def calcular_modulo(gradiente):
    suma = 0
    for i in range(0, len(gradiente)):
        suma = suma + gradiente[i] ** 2
    modulo = math.sqrt(suma)
    return modulo


def algoritmoVorazDescensoGradiente(A, b, x0, alpha, epsilon):
    A_t = traspuesta(A)
    A2_t = multiplicar_2DA_int(A_t, 2)
    A2T_A = multiplicar_A_B(A2_t, A)
    A2T_b = multiplicar_2DA_x(A2_t, b)
    x = x0
    gradiente = calcular_gradiente(A2T_A, A2T_b, x)
    while calcular_modulo(gradiente) > epsilon:
        x = restar(x, multiplicar_gradiente_alpha(gradiente, alpha))
        gradiente = calcular_gradiente(A2T_A, A2T_b, x)
    return x


n_m = lee_lista(2)
A = lee_lista2D(n_m[0], n_m[1])
b = lee_lista(n_m[0])
x0 = lee_lista_flotantes(n_m[1])
alpha = float(input())
epsilon = float(input())
x = algoritmoVorazDescensoGradiente(A, b, x0, alpha, epsilon)
imprime_lista(x)
