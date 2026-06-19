def investment_advice(income, expense):

    savings = income - expense

    if savings >= 50000:

        return """
AI Recommendation

• 40% SIP Investments
• 20% Fixed Deposits
• 20% Emergency Fund
• 20% Savings

Risk Level: Moderate to High
"""

    elif savings >= 20000:

        return """
AI Recommendation

• 30% SIP Investments
• 30% Fixed Deposits
• 20% Emergency Fund
• 20% Savings

Risk Level: Moderate
"""

    else:

        return """
AI Recommendation

• Build Emergency Fund First
• Reduce Expenses
• Maintain Savings Discipline

Risk Level: Low
"""