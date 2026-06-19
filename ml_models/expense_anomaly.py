def detect_expense_anomaly(expense):

    if expense > 10000:
        return "⚠️ Unusually High Expense Detected"

    elif expense > 5000:
        return "⚠️ Moderate Expense Alert"

    else:
        return "✅ Expense Looks Normal"