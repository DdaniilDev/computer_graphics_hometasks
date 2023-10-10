from PIL import Image
import matplotlib.pyplot as plt

image = Image.new('RGB', (500, 500))

def bresenham_line(x0, y0, x1, y1):
    dy = y1 - y0
    dx = x1 - x0
    is_vertical = abs(dy) > abs(dx)
    if is_vertical:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    if x1 < x0:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    current_y = y0
    error = 0
    for x in range(x0, x1 + 1):
        image.putpixel((current_y if is_vertical else x, x if is_vertical else current_y), (255, 255, 255))
        error += 2 * dy
        if error >= dx:
            current_y += 1
            error -= 2 * dx
        if error < -dx:
            current_y -= 1
            error += 2 * dx



def bresenham_circle(x, y, radius):
    x_ = 0
    y_ = radius
    f0 = 3 - 2 * radius
    while y_ >= x_:
        image.putpixel((x + x_, y + y_), (255, 255, 255))
        image.putpixel((x - x_, y + y_), (255, 255, 255))
        image.putpixel((x + x_, y - y_), (255, 255, 255))
        image.putpixel((x - x_, y - y_), (255, 255, 255))
        image.putpixel((x + y_, y + x_), (255, 255, 255))
        image.putpixel((x - y_, y + x_), (255, 255, 255))
        image.putpixel((x + y_, y - x_), (255, 255, 255))
        image.putpixel((x - y_, y - x_), (255, 255, 255))
        x_ += 1
        if f0 > 0:
            y_ -= 1
            f0 += 4 * x_ - 4 * y_ + 10
        else:
            f0 += 4 * x_ + 6


def main():
    print("Введите название фигуры, которую хотите построить по алгоритму Брезензхема:\n1) Для линии\n2) Для "
          "круга\nВвод: ")
    choose = int(input())
    match choose:
        case 1:
            print("Введите координаты для двух точек: ")
            first_point_x = int(input())
            first_point_y = int(input())
            second_point_x = int(input())
            second_point_y = int(input())
            bresenham_line(first_point_x, first_point_y, second_point_x, second_point_y)
            plt.title("Bresenham algorithm - Line")
            plt.imshow(image)
            plt.show()
        case 2:
            print("Введите координаты и радиус: ")
            x = int(input())
            y = int(input())
            radius = int(input())
            bresenham_circle(x, y, radius)
            plt.title("Bresenham algorithm - Circle")
            plt.imshow(image)
            plt.show()
        case _:
            print("Ошибка")


if __name__ == "__main__":
    main()
