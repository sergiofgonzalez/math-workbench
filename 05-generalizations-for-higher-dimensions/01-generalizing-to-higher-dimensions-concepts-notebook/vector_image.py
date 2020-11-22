from PIL import Image
from vector import Vector
from abc import abstractmethod

class ImageVector(Vector):

    @classmethod
    @abstractmethod
    def size(cls):
        """A tuple with the image dimensions (width, height)
        """
        pass

    def __init__(self, input):
        """The constructor accepts the path of an image file, which will get resized
        to the given size, and converted to a list of pixels, with each pixel being a
        triple (r, g, b).

        The constructor also accepts directly a list of pixels as a fallback when
        opening the image file fails.
        """
        try:
            img = Image.open(input).resize(self.__class__.size())
            if img.mode != 'RGB':
                rgb_img = img.convert('RGB')                
            self.pixels = rgb_img.getdata()
        except:
            self.pixels = input

    def image(self):
        """Prepares a PIL image, in RGB format with the given size and reconstruct
        the image from the pixels stored in the object
        """
        # create a blank image
        img = Image.new('RGB', self.__class__.size())

        # in the constructor we use PIL methods, here we're doing it manually
        # inspecting if the pixel data contains more than 3 channels
        if len(self.pixels) > 0:
            pixel_data_contains_alpha_channel = len(self.pixels[0]) == 4

        rgb_pixel_data = [(int(r), int(g), int(b)) for r, g, b, _ in self.pixels] if pixel_data_contains_alpha_channel else [(int(r), int(g), int(b)) for r, g, b in self.pixels]

        # put the pixel data into it
        img.putdata(rgb_pixel_data)
        return img

    def  add(self, other):
        """Adds an image by adding their (r, g, b) components of their pixels
        """
        return self.__class__(
            [(r1 + r2, g1 + g2, b1 + b2) for (r1, g1, b1), (r2, g2, b2) in zip(self.pixels, other.pixels)]
        )

    def scale(self, scalar):
        """Scales an image by an scalar by multiplying their (r, g, b) components
        by the given scalar
        """
        return self.__class__(
            [(scalar * r, scalar * g, scalar * b) for r, g, b in self.pixels]
        )
    
    @classmethod
    def zero(cls):
        """Returns an image of the given size in which the (r, g, b) components 
        of all the pixels are set to zero.
        """
        width, height = cls.size()
        total_pixels = width * height
        return cls(
            [(0, 0, 0) for _ in range(0, total_pixels)]
        )

    def _repr_png_(self):
        """Function that allows Jupyter notebooks to display PIL images inline.
        """
        return self.image()._repr_png_()