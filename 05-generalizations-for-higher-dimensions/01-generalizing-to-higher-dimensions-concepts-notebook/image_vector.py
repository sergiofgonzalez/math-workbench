from PIL import Image
from vector import Vector
import sys

class ImageVector(Vector):
    size = (300, 300)

    def __init__(self, input):
        try:
            # the constructor accepts the name of an image file,
            # which gets resized to 300x300 and converted to a list
            # of pixels with each pixel being a triple r, g, b
            img = Image.open(input).resize(ImageVector.size)
            self.pixels = img.getdata()
        except:
            # print("Unexpected error:", sys.exc_info()[0])
            # accept directly a list of pixels as a fallback
            self.pixels = input

    def image(self):
        # prepare a PIL image, in RGB format with size 300x300
        img = Image.new('RGB', ImageVector.size)

        # reconstruct the image from the pixels stored in the object
        img.putdata([(int(r), int(g), int(b)) for (r, g, b) in self.pixels])
        return img

    def add(self, img2):
        return ImageVector([(r1+r2,g1+g2,b1+b2) 
                            for ((r1,g1,b1),(r2,g2,b2)) 
                            in zip(self.pixels,img2.pixels)])

    def scale(self, scalar):
        return ImageVector([(scalar * r, scalar * g, scalar * b) 
            for (r, g, b) in self.pixels])

    @classmethod
    def zero(cls):
        total_pixels = cls.size[0] * cls.size[1]
        return ImageVector([(0, 0, 0) for _ in range(0, total_pixels)])

    def _repr_png_(self):
        # implementing a _repr_png_ function allows Jupyter notebooks to
        # display PIL images inline
        return self.image()._repr_png_()
