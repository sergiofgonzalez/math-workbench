import unittest
from test_vector2d import Vec2TestCase
from test_vector3d import Vec3TestCase
from test_vector6d import Vec6TestCase

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(Vec2TestCase))
    suite.addTests(unittest.makeSuite(Vec3TestCase))
    suite.addTests(unittest.makeSuite(Vec6TestCase))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())