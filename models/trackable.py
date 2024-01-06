class Trackable:
    def __init__(self, value, day_of_week, date_of_month, frequency):
        self.value = value
        self.day_of_week = day_of_week
        self.date_of_month = date_of_month
        self.frequency = frequency

    def get_value(self):
        return self.value

    def set_value(self, val):
        self.value = val

    def get_day_of_week(self):
        return self.day_of_week

    def set_day_of_week(self, val):
        self.day_of_week = val

    def get_date_of_month(self):
        return self.date_of_month

    def set_date_of_month(self, val):
        self.date_of_month = val

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, val):
        self.frequency = val

    def to_string(self):
        return (f'value: {self.get_value()}\n'
                f'day_of_week: {self.get_day_of_week()}\n'
                f'date_of_month: {self.get_date_of_month()}\n'
                f'frequency: {self.get_frequency()}'
                )
