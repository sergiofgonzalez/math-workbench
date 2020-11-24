from vector_image import ImageVector

class ImageVector_300x300(ImageVector):

    @classmethod
    def size(cls):
        """Returns a tuple with the size of this image (width, height)
        """
        return (300, 300)
