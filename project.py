from constant import *


class Project:
    def __init__(self, start_date, end_date, city_type):
        self.start_date = start_date
        self.end_date = end_date
        self.city_type = city_type

    def is_active(self, date):
        """
        returns true if date is within start and end date of project
        """
        return self.start_date <= date <= self.end_date
