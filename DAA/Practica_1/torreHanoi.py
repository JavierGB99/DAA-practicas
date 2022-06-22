def torres_hanoi(piezas,x,y,z):
    if piezas == 1:
        print("Mueve disco", piezas, "desde torre", x, "a torre", y)
        print("Mueve disco", piezas, "desde torre", y, "a torre", z)
    else:
        if piezas == 2:
            torres_hanoi(piezas-1,x,y,z)
            print("Mueve disco", piezas, "desde torre", x, "a torre", y)
            torres_hanoi(piezas-1, z, y, x)
            print("Mueve disco", piezas, "desde torre", y, "a torre", z)
            torres_hanoi(piezas-1, x, y, z)
        else:
            torres_hanoi(piezas - 1, x, y, z)
            print("Mueve disco", piezas, "desde torre", x, "a torre", y)
            torres_hanoi(piezas - 2, z, y, x)
            print("Mueve disco", piezas - 1, "desde torre", z, "a torre", y)
            torres_hanoi(piezas - 2, x, y, z)
            print("Mueve disco", piezas - 1, "desde torre", y, "a torre", x)
            torres_hanoi(piezas - 2, z, y, x)
            print("Mueve disco", piezas, "desde torre", y, "a torre", z)
            torres_hanoi(piezas - 1, x, y, z)


piezas = int(input())
if piezas<=9 or piezas >0:
    torres_hanoi(piezas,1,2,3)
