import unittest
from test_vector0d import Vec0TestCase
from test_vector1d import Vec1TestCase
from test_vector2d import Vec2TestCase
from test_vector3d import Vec3TestCase
from test_vector5d import Vec5TestCase
from test_vector6d import Vec6TestCase
from test_vector_car_for_sale import VectorCarForSaleTest
from test_vector_function import VectorFunctionTestCase
from test_vector_function2 import VectorFunction2TestCase
from test_matrix_2x2 import Matrix2x2TestCase
from test_matrix_5x3 import Matrix5x3TestCase
from test_linear_map_3d_to_5d import LinearMap_3d_to_5d_TestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(Vec0TestCase))
    suite.addTests(unittest.makeSuite(Vec1TestCase))    
    suite.addTests(unittest.makeSuite(Vec2TestCase))
    suite.addTests(unittest.makeSuite(Vec3TestCase))
    suite.addTests(unittest.makeSuite(Vec5TestCase))
    suite.addTests(unittest.makeSuite(Vec6TestCase))
    suite.addTests(unittest.makeSuite(VectorCarForSaleTest))
    # suite.addTests(unittest.makeSuite(VectorFunctionTestCase)) # contains blocking plots
    suite.addTests(unittest.makeSuite(VectorFunction2TestCase))
    suite.addTests(unittest.makeSuite(Matrix2x2TestCase))
    suite.addTests(unittest.makeSuite(Matrix5x3TestCase))
    suite.addTests(unittest.makeSuite(LinearMap_3d_to_5d_TestCase))            

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())