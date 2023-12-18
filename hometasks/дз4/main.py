from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def fill_polygon(img, seed):
    stack = [seed]

    while stack:
        x, y = stack.pop()

        if img[x, y] == 0:
            img[x, y] = 1
            neighbors = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]

            for nx, ny in neighbors:
                if 0 <= nx < img.shape[0] and 0 <= ny < img.shape[1]:
                    stack.append((nx, ny))


image_size = 10
img = np.zeros((image_size, image_size))


polygon_points = [(2, 2), (8, 2), (8, 8), (5, 5), (2, 8)]


polygon = np.array(polygon_points)
plt.fill(polygon[:, 0], polygon[:, 1], color='blue')
seed_point = (4, 4)
fill_polygon(img, seed_point)

plt.imshow(img, cmap='gray', origin='lower')
plt.show()