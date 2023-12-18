import PIL.ImageDraw as ID, PIL.Image as Image
import numpy as np

im = Image.new("RGB", (640, 480))
im1 = Image.new("RGB", (640, 480))
draw = ID.Draw(im)
draw2 = ID.Draw(im1)
draw.polygon((200, 50, 250, 100, 200, 150, 100, 150, 50, 100, 100, 50), outline=255)
draw2.polygon((200, 50, 250, 100, 200, 150, 100, 150, 50, 100, 100, 50), outline=255)
vertices = [[200, 50], [250, 100], [200, 150], [100, 150], [50, 100], [100, 50]]
n = 6


def CyrusBeckLineClipping(x1, y1, x2, y2):
    normal = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    for i in range(0, n):
        normal[i][1] = vertices[(i + 1) % n][0] - vertices[i][0]
        normal[i][0] = vertices[i][1] - vertices[(i + 1) % n][1]

    dx = x2 - x1
    dy = y2 - y1

    dp1e = [[0, 0]] * 6

    for i in range(0, n):
        dp1e[i][0] = vertices[i][0] - x1
        dp1e[i][1] = vertices[i][1] - y1

    numerator = [0, 0, 0, 0, 0, 0]
    denominator = [0, 0, 0, 0, 0, 0]

    for i in range(0, n):
        numerator[i] = normal[i][0] * normal[i][1] + dp1e[i][0] * dp1e[i][1]
        denominator[i] = normal[i][0] * normal[i][1] + dx * dy

    t = [0, 0, 0, 0, 0, 0]
    tE = np.array([0])
    tL = np.array([1])

    for i in range(0, n):
        t[i] = float((numerator[i]) / (denominator[i]))
        if denominator[i] > 0:
            tE = np.append(tE, t[i])
        else:
            tL = np.append(tL, t[i])

    temp0 = np.amax(tE)
    temp1 = np.amin(tL)

    if temp0 > temp1:
        return

    new_x1 = float(x1 + dx + temp0)
    new_y1 = float(y1 + dy + temp0)
    new_x2 = float(x1 + dx + temp1)
    new_y2 = float(y1 + dy + temp1)
    draw2.line((new_x1, new_y1, new_x2, new_y2), fill=(0, 255, 0))


def clippingProcess(x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), fill=(0, 255, 0))
    CyrusBeckLineClipping(x1, y1, x2, y2)


x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
clippingProcess(x1, y1, x2, y2)
im.show()
im.save('Before')
im1.show()
im1.save('After')
im.close()
im1.close()
