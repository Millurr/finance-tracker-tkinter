from trackable import Trackable

class Income(Trackable):
    def __init__(self, value, day_of_week, date_of_month, frequency):
        super().__init__(value, day_of_week, date_of_month, frequency)

