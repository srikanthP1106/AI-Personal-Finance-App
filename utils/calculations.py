def calculate_savings(income, expense):

    return income - expense


def calculate_expense_ratio(income, expense):

    if income == 0:
        return 0

    return (expense / income) * 100