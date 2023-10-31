import math
import numpy as np
import matplotlib.pyplot as plt

x1, y1 = map(float, input("Координаты начальной точки прямой (x y): ").split())
x2, y2 = map(float, input("Координаты конечной точки прямой (x y): ").split())
x_center, y_center = map(float, input("Координаты точки вращения (x y): ").split())

set_angle = math.radians(180)

matrix_for_rotation = np.array([[math.cos(set_angle), -math.sin(set_angle)],
                            [math.sin(set_angle), math.cos(set_angle)]])

x1 -= x_center
y1 -= y_center
x2 -= x_center
y2 -= y_center

new_x1, new_y1 = np.dot(matrix_for_rotation, [x1, y1])
new_x2, new_y2 = np.dot(matrix_for_rotation, [x2, y2])

new_x1 += x_center
new_y1 += y_center
new_x2 += x_center
new_y2 += y_center


if __name__ == "__main__":
    plt.figure()
    plt.xlim(-250, 250)
    plt.ylim(-250, 250)
    plt.plot([x1, x2], [y1, y2])
    plt.plot([new_x1, new_x2], [new_y1, new_y2])
    plt.scatter(x_center, y_center)
    plt.title('Поворот прямой вокруг точки')
    plt.grid(True)
    plt.show()
