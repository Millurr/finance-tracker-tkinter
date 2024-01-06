

class Computations:
    def __init__(self):
        pass

    def get_total_income(self, income):
        return sum(income)

    def get_total_expenses(self, expenses):
        return sum(expenses)

    def get_net_income(self, income, expenses):
        return sum(income) - sum(expenses)