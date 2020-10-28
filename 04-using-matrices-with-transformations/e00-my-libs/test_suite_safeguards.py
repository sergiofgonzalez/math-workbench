import unittest
from test_safeguards_my_vectors import MyVectorsTestCase
from test_safeguards_my_matrices import MyMatricesTestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(MyVectorsTestCase))
    suite.addTests(unittest.makeSuite(MyMatricesTestCase))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())