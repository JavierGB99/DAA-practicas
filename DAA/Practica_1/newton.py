def newton(x, resultado):
    if abs(resultado ** 2 -x) <= 0.000001:
        return resultado
    else:
        return newton(x, (resultado**2+x)/(2*resultado))

def insertSortedList(S, elemento, acumulador):
    if len(S) == 1 or len(S)-1 == acumulador:
        if S[acumulador] >= elemento:
            S[acumulador] = elemento
            return S
        else:
            S[acumulador]=elemento
            return S
    else:
        if S[acumulador] >= elemento:
            for i in reversed(range((len(S)-1))):
                S[i+1]=S[i]
            S[acumulador]=elemento
            return S
        else:
            insertSortedList(S, elemento, acumulador + 1)


num = float(input())
resultant = newton(num, num)
print('%.4f'%resultant)

