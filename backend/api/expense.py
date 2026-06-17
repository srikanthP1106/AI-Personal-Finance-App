from fastapi import APIRouter
from database.db import connection, cursor
from backend.schemas.expense import ExpenseCreate

router = APIRouter()

@router.post("/expense")
def add_expense(amount: float, category: str):

    expense = {
        "amount": amount,
        "category": category
    }

    cursor.execute(
        "INSERT INTO expense (amount, category) VALUES (%s, %s)",
        (amount, category)
    )

    connection.commit()

    return {
        "message": "Expense Added Successfully",
        "data": expense
    }


@router.get("/expense")
def get_expense():

    cursor.execute("SELECT * FROM expense")

    data = cursor.fetchall()

    return data