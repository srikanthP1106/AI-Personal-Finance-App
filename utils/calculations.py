def calculate_savings(income, expense):

    return income - expense


def calculate_expense_ratio(income, expense):

    if income == 0:
        return 0

    return (expense / income) * 100


def calculate_financial_health_score(income, expense):

    if income == 0:
        return 0

    savings = income - expense

    savings_ratio = (savings / income) * 100

    if savings_ratio >= 70:
        return 95

    elif savings_ratio >= 50:
        return 85

    elif savings_ratio >= 30:
        return 70

    else:
        return 50