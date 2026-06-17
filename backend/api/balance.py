from fastapi import APIRouter
from database.db import cursor

router = APIRouter()


@router.get("/balance")
def get_balance():

    cursor.execute("SELECT SUM(amount) FROM income")
    total_income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM expense")
    total_expense = cursor.fetchone()[0] or 0

    balance = total_income - total_expense

    return {
        "total_income": float(total_income),
        "total_expense": float(total_expense),
        "balance": float(balance)
    }