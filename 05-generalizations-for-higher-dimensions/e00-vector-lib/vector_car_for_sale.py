from datetime import datetime
from vector import Vector
from json import loads, dumps
from pathlib import Path

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

    @classmethod
    def get_carForSale_list_from_json(cls, json_file_path):
        def parse_date(s):
            input_format = '%m/%d - %H:%M'
            # .replace will set the year in the datetime object to 2018
            dt = datetime.strptime(s, input_format).replace(year = 2018)
            return dt

        file_contents_as_text = Path(json_file_path).read_text()
        objects_from_file = loads(file_contents_as_text)
        cleaned_objects = []

        # some_list[1:] creates an iterator from the second element
        for car_object in objects_from_file[1:]:
            try:
                row = CarForSale(int(car_object[1]), float(car_object[3]), float(car_object[4]), parse_date(car_object[6]), car_object[2], car_object[5], car_object[7], car_object[8])
                cleaned_objects.append(row)
            except:
                pass

        return cleaned_objects
