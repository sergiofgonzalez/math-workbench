from datetime import datetime
from vector import Vector

class CarForSale(Vector):
    reference_date = datetime(2018, 11, 30, 12) # 30-Nov-2018-12:00:00

    def __init__(self, model_year, mileage, price, posted_datetime, model='(virtual)', source='(virtual)', location='(virtual)', description='(virtual)'):
        self.model_year = model_year
        self.mileage = mileage
        self.price = price
        self.posted_datetime = posted_datetime
        self.model = model
        self.source = source
        self.location = location
        self.description = description

    def add(self, other):
        def add_dates(d1, d2):
            age1 = CarForSale.reference_date - d1
            age2 = CarForSale.reference_date - d2
            sum_age = age1 + age2
            return CarForSale.reference_date - sum_age

        return CarForSale(
            self.model_year + other.model_year,
            self.mileage + other.mileage,
            self.price + other.price,
            add_dates(self.posted_datetime, other.posted_datetime)
        )

    def scale(self, scalar):
        def scale_date(d):
            age = CarForSale.reference_date - d
            return CarForSale.reference_date - (scalar * age)

        return CarForSale(
            scalar * self.model_year,
            scalar * self.mileage,
            scalar * self.price,
            scale_date(self.posted_datetime)
        )

    @classmethod
    def zero(cls):
        return CarForSale(0, 0, 0, CarForSale.reference_date)