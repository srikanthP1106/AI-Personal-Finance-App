from fastapi import APIRouter
from database.db import connection, cursor
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

    cursor.execute("SELECT * FROM income")

    data = cursor.fetchall()

    return data