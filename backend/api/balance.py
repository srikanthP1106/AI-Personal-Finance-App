from fastapi import APIRouter
from database.db import cursor

router = APIRouter()


@router.get("/balance")
def get_balance():

    cursor.execute("SELECT SUM(amount) FROM income")
    total_income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM expense")
    total_expense = cursor.fetchone()[0] or 0

    cursor.execute("SELECT COUNT(*) FROM income")
    income_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM expense")
    expense_count = cursor.fetchone()[0]

    balance = total_income - total_expense

    return {
        "total_income": float(total_income),
        "total_expense": float(total_expense),
        "balance": float(balance),
        "income_count": income_count,
        "expense_count": expense_count
    }