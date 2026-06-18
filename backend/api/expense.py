from fastapi import APIRouter
from database.db import connection, cursor
from backend.schemas.expense import ExpenseCreate
from backend.crud.expense_crud import get_all_expense

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

    return get_all_expense()

@router.put("/expense/{expense_id}")
def update_expense(expense_id: int, amount: float, category: str):

    cursor.execute(
        "UPDATE expense SET amount = %s, category = %s WHERE id = %s",
        (amount, category, expense_id)
    )

    connection.commit()

    return {
        "message": "Expense Updated Successfully"
    }


@router.delete("/expense/{expense_id}")
def delete_expense(expense_id: int):

    cursor.execute(
        "DELETE FROM expense WHERE id = %s",
        (expense_id,)
    )

    connection.commit()

    return {
        "message": "Expense Deleted Successfully"
    }