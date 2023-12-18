from PIL import Image


def sobelFilter(image, width, height):
    kernel_x = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
    kernel_y = [-1, -2, -1, 0, 0, 0, 1, 2, 1]
    x_range = [0 for x in range(len(image))]
    y_range = [0 for x in range(len(image))]
    iterator = 0
    while iterator + 1 < width - 1:
        for j in range(1, height - 1):
            for k in range(-4, 5, 1):
                x_range[j * width + iterator] += image[j * width + iterator + k] * kernel_x[k + 4]
                y_range[j * width + iterator] += image[j * width + iterator + k] * kernel_y[k + 4]
        iterator += 1
    gradient_magn = list(map(lambda a, b: int(pow((pow(a, 2) + pow(b, 2)), 0.5)), x_range, y_range))
    return gradient_magn


path = 'venv/example.png'
with Image.open(path) as working_image:
    condition = 'L'
    tmp_array = working_image.convert(condition).getdata()
    result = sobelFilter(tmp_array, working_image.size[0], working_image.size[1])
    new_image = Image.new(mode="RGB", size=(working_image.size[0], working_image.size[1]))
    new_image.putdata(result)
    new_im = new_image.convert(condition)
    new_im.save('result.png')
    new_im.close()
