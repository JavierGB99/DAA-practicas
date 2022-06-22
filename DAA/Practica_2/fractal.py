import matplotlib.pyplot as plt
import numpy as np


def dibuja_triangulo(ax, p, distance, h):
    pivot_left = (p[0], p[1])
    pivot_right = (p[0] + distance, p[1])
    pivot_top = (p[0] + distance / 2, p[1] + h)
    points = np.array([pivot_left, pivot_right, pivot_top])
    pivot = plt.Polygon(points, closed=True)
    ax.add_patch(pivot)


def fractal_triangles(ax, p, b, h, n):
    if n == 0:
        dibuja_triangulo(ax, p, b, h)
    else:
        fractal_triangles(ax, p, b, h, n - 1)

        p = [p[0] - (2 ** (n - 1)) * (b // 2), p[1] - (2 ** (n - 1)) * h]
        fractal_triangles(ax, p, b, h, n - 1)

        p = [p[0] + (2 ** (n - 1)) * b, p[1]]
        fractal_triangles(ax, p, b, h, n - 1)


fig = plt.figure()
fig.patch.set_facecolor('white')
ax = plt.gca()
p = [0, 0]
b = 6
h = 4
#n cambia el numero de iteraciones
n = 4
fractal_triangles(ax, p, b, h, n)
plt.axis('equal')
plt.axis('off')
plt.show()
