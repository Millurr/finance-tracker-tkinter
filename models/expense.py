from trackable import Trackable
import json


def load_categories():
    f = open('../data/expense_categories.json')
    return json.load(f)


class Expense(Trackable):
    def __init__(self, value, day_of_week, date_of_month, frequency):
        super().__init__(value, day_of_week, date_of_month, frequency)
        self.categories = load_categories()

    def to_string(self):
        return (f'{super().to_string()}\n'
                f'categories: {self.categories}')


if __name__ == '__main__':
    expense = Expense(10, 1, [2,3], 1)
    print(expense.to_string())