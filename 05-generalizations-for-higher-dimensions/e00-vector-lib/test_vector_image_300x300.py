import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose
from random import randint
from test_vector import VectorTestCase
from vector_image_300x300 import ImageVector_300x300

class ImageVector_300x300_TestCase(VectorTestCase):
    def random_color_value(self):
        value = randint(0, 255)
        return value

    def random_image_pixels(self):
        width, height = ImageVector_300x300.size()
        pixels = [(self.random_color_value(), self.random_color_value(), self.random_color_value()) for _ in range(0, width * height)]
        return pixels

    def approx_equal(self, v, w):
        if (not ImageVector_300x300 in v.__class__.mro()) or (not ImageVector_300x300 in w.__class__.mro()):
            return False

        if not v.__class__.size() == w.__class__.size():
            return False
        
        # next one was my first approach, but the author's one is more Pythonic
        # return all(isclose(v_r, w_r) and isclose(v_g, w_g) and isclose(v_b, w_b) for (v_r, v_g, v_b), (w_r, w_g, w_b) in zip(v.pixels, w.pixels))        
        return all([isclose(v_rgb_component, w_rgb_component) for v_rgb, w_rgb in zip(v.pixels, w.pixels) for v_rgb_component, w_rgb_component in zip(v_rgb, w_rgb)])



    # note that tests displaying images can only be executed one by one 
    # as image.show() is not blocking and uses a tmp location that gets
    # overwritten



    # def test_build_image_passing_path(self):
    #     v = ImageVector_300x300('./images/001.png')
    #     v.image().show()

    # def test_build_image_passing_pixels(self):
    #     v = ImageVector_300x300('./images/002.png')
    #     pixels_with_no_r = [(0, g, b, alpha) for (_, g, b, alpha) in v.pixels]
    #     w = ImageVector_300x300(pixels_with_no_r)
    #     w.image().show()

    # def test_add_happy_path(self):
    #     v = ImageVector_300x300('./images/001.png')
    #     w = ImageVector_300x300('./images/002.png')
    #     sum_image = v + w
    #     sum_image.image().show()

    # def test_scale_happy_path(self):
    #     w = ImageVector_300x300('./images/002.png')
    #     scaled_image = 0.5 * w
    #     scaled_image.image().show()

    # def test_linear_combination_happy_path(self):
    #     v = ImageVector_300x300('./images/001.png')
    #     w = ImageVector_300x300('./images/002.png')
    #     linear_combo_image = 0.25 * v + 0.75 * w
    #     linear_combo_image.image().show()        

    # added in exercise 6.20
    # def test_zero_vector(self):
    #     v = ImageVector_300x300('./images/001.png')
    #     zero = ImageVector_300x300.zero()

    #     result_image = v + zero
    #     result_image.image().show()

    # added in exercise 6.21
    # def test_random_image(self):
    #     v = ImageVector_300x300(self.random_image_pixels())
    #     v.image().show()

    def test_approx_equal(self):
        v = ImageVector_300x300(self.random_image_pixels())
        w = ImageVector_300x300(v.pixels)
        self.assertTrue(self.approx_equal(v, w))

    # This test takes around 2 mins
    # def test_ImageVector_300x300_is_vector_space(self):
    #     for _ in range(0, 100):
    #         a, b = self.random_scalar(), self.random_scalar()
    #         u, v, w = ImageVector_300x300(self.random_image_pixels()), ImageVector_300x300(self.random_image_pixels()), ImageVector_300x300(self.random_image_pixels())
    #         self.check_vector_space_rules(self.approx_equal, a, b, u, v, w)


if __name__ == '__main__':
    unittest.main()
