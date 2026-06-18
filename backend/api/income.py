from fastapi import APIRouter
from database.db import connection, cursor
from backend.crud.income_crud import get_all_income
from backend.schemas.income import IncomeCreate

router = APIRouter()

income_data = []


@router.post("/income")
def add_income(amount: float, source: str):

    income = {
        "amount": amount,
        "source": source
    }

    cursor.execute(
        "INSERT INTO income (amount, source) VALUES (%s, %s)",
        (amount, source)
    )

    connection.commit()

    return {
        "message": "Income Added Successfully",
        "data": income
    }


@router.get("/income")
def get_income():

    return get_all_income()
@router.put("/income/{income_id}")
def update_income(income_id: int, amount: float, source: str):

    cursor.execute(
        "UPDATE income SET amount = %s, source = %s WHERE id = %s",
        (amount, source, income_id)
    )

    connection.commit()

    return {
        "message": "Income Updated Successfully"
    }


@router.delete("/income/{income_id}")
def delete_income(income_id: int):

    cursor.execute(
        "DELETE FROM income WHERE id = %s",
        (income_id,)
    )

    connection.commit()

    return {
        "message": "Income Deleted Successfully"
    }