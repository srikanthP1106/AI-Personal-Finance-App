from fastapi import APIRouter
from database.db import cursor

router = APIRouter()


@router.get("/monthly-summary")
def monthly_summary():

    cursor.execute("SELECT SUM(amount) FROM income")
    total_income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM expense")
    total_expense = cursor.fetchone()[0] or 0

    savings = total_income - total_expense

    return {
        "month": "Current Month",
        "income": float(total_income),
        "expense": float(total_expense),
        "savings": float(savings)
    }