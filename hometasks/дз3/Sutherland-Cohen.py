from PIL import Image
import PIL.ImageDraw as ID
import matplotlib.pyplot as plt
image1 = Image.new('RGB', (1000, 1000))
image2 = Image.new('RGB', (1000, 1000))

x_max = 400.0
y_max = 300.0
x_min = 200.0
y_min = 200.0

line_draw = ID.Draw(image1)
line_draw2 = ID.Draw(image2)

# polygon(x1, y1, x2, y2, x3, y3, x4, y4)
line_draw.polygon((200, 200, 400, 200, 400, 300, 200, 300), outline=255)
line_draw2.polygon((200, 200, 400, 200, 400, 300, 200, 300), outline=255)

def computeCode(x, y):
    code = 0
    if x < x_min:
        code |= 1
    elif x > x_max:
        code |= 2
    if y < y_min:
        code |= 4
    elif y > y_max:
        code |= 8
    return code

def cohenSutherlandClip(x1, y1, x2, y2):
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False

    while True:

        if code1 == 0 and code2 == 0:
            accept = True
            break

        elif (code1 & code2) != 0:
            break

        else:
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
            if code_out & 8:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & 4:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & 2:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & 1:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)
            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)
    if accept:
        line_draw2.line((x1, y1, x2, y2), fill=(0, 0, 255))
    else:
        print("Ошибка")


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
        image1.putpixel((current_y if is_vertical else x, x if is_vertical else current_y), (255, 255, 255))
        error += 2 * dy
        if error >= dx:
            current_y += 1
            error -= 2 * dx
        if error < -dx:
            current_y -= 1
            error += 2 * dx

def comp(x1, y1, x2, y2):
    line_draw.line((x1, y1, x2, y2), fill=(0, 255, 0))
    cohenSutherlandClip(x1, y1, x2, y2)

if __name__ == "__main__":
    x1 = int(input("Точка x1: "))
    y1 = int(input("Точка y1: "))
    x2 = int(input("Точка x2: "))
    y2 = int(input("Точка y2: "))
    comp(x1, y1, x2, y2)
    plt.title("Cohen algorithm")
    plt.imshow(image2)
    plt.show()
