from enum import Enum


class ExpenseCategories(Enum):
    GROCERY = (1, 'Grocery')
    BILL = (2, 'Bill')
    UTILITY = (3, 'Utility')
    CREDITCARD = (4, 'Credit Card')
    LOAN = (5, 'Loan')
