from vector_image_300x300 import ImageVector_300x300
# from random import randint

# def random_color_value():
#     return randint(0, 255)

# width, height = ImageVector_300x300.size()
# pixels = [(random_color_value(), random_color_value(), random_color_value()) for _ in range(0, width * height)]

# # ImageVector_300x300(pixels).image().show()

# this one works OK, although it is a bit ugly
def get_ImageVector_300x300_from_grayscale_30x30(grayscale_30x30_pixels):
    width, height = ImageVector_300x300.size()
    pixels_300 = []
    for pixel_position in range(0, width * height):
        x = pixel_position % width
        y = pixel_position // width
        x_30 = x // 10
        y_30 = y // 10
        pixel_pos_30 = x_30 + (y_30 * 30)
        brightness = grayscale_30x30_pixels[pixel_pos_30]
        pixels_300.append((brightness, brightness, brightness))
    return ImageVector_300x300(pixels_300)

# let's test it

# grayscale_30x30_pixels = [i % 256 for i in range(0, 30 * 30)]
# get_ImageVector_300x300_from_grayscale_30x30(grayscale_30x30_pixels).image().show()


# this one only works for first row
def to_grayscale_30x30(image_300x300):
    width = 30
    height = 30
    grayscale_pixels = []
    for pixel_position in range(0, width * height):
        x_init = (pixel_position * 10) % 300
        x_end = x_init + 9
        y_init = (pixel_position // 30) * 10
        y_end = y_init + 9
        sum_rgb = 0
        for y in range(y_init, y_end + 1):
            for x in range(x_init, x_end + 1):
                pos_300 = x + (y * 300)
                r, g, b = image_300x300.pixels[pos_300]
                sum_rgb += (r + g + b)
        brightness = sum_rgb // (10 * 10 * 3)
        grayscale_pixels.append(brightness)
    return grayscale_pixels


beach = ImageVector_300x300('./002.png')

# get_ImageVector_300x300_from_grayscale_30x30(to_grayscale_30x30(beach)).image().show()

image_size = (300, 300)
total_pixels = image_size[0] * image_size[1]
square_count = 30
square_width = 10

def ij(n):
    return (n // image_size[0], n % image_size[1])

def to_lowres_grayscale(img):
    matrix = [
        [0 for i in range(0, square_count)] for j in range(0, square_count)
    ]
    for (n, p) in enumerate(img.pixels):
        i, j = ij(n)
        weight = 1.0 / (3 * square_width * square_width)
        matrix[i // square_width][j // square_width] += (sum(p) * weight)
    return matrix

def from_lowres_grayscale(matrix):
    def lowres(pixels, ij):
        i, j = ij
        return pixels[i // square_width][j // square_width]
    def make_highres():
        triple = lambda x: (x, x, x)
        return ImageVector_300x300([triple(lowres(matrix, ij(n))) for n in range(0, total_pixels)])

    return make_highres()

# matrix = to_lowres_grayscale(beach)
# pix_30x30 = []
# for row in matrix:
#     for pix in row:
#         pix_30x30.append(int(pix))

# to_grayscale_30x30(beach)
# get_ImageVector_300x300_from_grayscale_30x30(pix_30x30).image().show()

from_lowres_grayscale(to_lowres_grayscale(beach)).image().show()