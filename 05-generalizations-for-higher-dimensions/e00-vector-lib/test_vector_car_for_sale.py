import unittest  # https://docs.python.org/3/library/unittest.html
from math import isclose
from random import uniform, randint, randrange
from vector_car_for_sale import CarForSale
from test_vector import VectorTestCase
from datetime import datetime, timedelta

class VectorCarForSaleTest(VectorTestCase):
    def get_random_datetime(self):
        start_date = datetime(2000, 1, 1, randint(0, 23), randint(0, 59), randint(0, 59))
        end_date = datetime(2018, 1, 1, randint(0, 23), randint(0, 59), randint(0, 59))
        time_between_dates = end_date - start_date
        days_betwwen_dates = time_between_dates.days
        random_number_of_days = randrange(days_betwwen_dates)
        random_date = start_date + timedelta(days=random_number_of_days)
        return random_date

    def random_coordinates(self):
        model_year = randint(2000, 2018)
        mileage = uniform(0, 500000)
        price = randint(10000, 75000)
        posted_datetime = self.get_random_datetime()
        return [model_year, mileage, price, posted_datetime]

    def approx_equal(self, v, w):
        if (not CarForSale in v.__class__.mro()) or (not CarForSale in w.__class__.mro()):
            raise TypeError('approx_equal requires compatible CarForSale vectors')        
        
        time_between_dates = v.posted_datetime - w.posted_datetime

        return isclose(v.model_year, w.model_year) and isclose(v.mileage, w.mileage) and isclose(v.price, w.price) and isclose(time_between_dates.total_seconds(), 0.0, abs_tol=0.001)

    def test_get_carForSale_list_from_json(self):
        cars = CarForSale.get_carForSale_list_from_json('./cargraph.json')
        self.assertEqual(len(cars), 41)

    def test_CarForSale_is_vector_space(self):
        for _ in range(0, 1000):
            a, b = self.random_scalar(), self.random_scalar()
            u, v, w = CarForSale(*self.random_coordinates()), CarForSale(*self.random_coordinates()), CarForSale(*self.random_coordinates())
            self.check_vector_space_rules(self.approx_equal, a, b, u, v, w)

if __name__ == '__main__':
    unittest.main()    