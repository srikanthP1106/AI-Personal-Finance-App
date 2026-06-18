def investment_advice(income, expense):

    savings = income - expense

    if savings > 50000:
        return "You can invest aggressively."

    elif savings > 20000:
        return "Moderate investment strategy recommended."

    else:
        return "Focus on building savings first."