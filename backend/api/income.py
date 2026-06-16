from fastapi import APIRouter

router = APIRouter()

income_data = []

@router.post("/income")
def add_income(amount: float, source: str):

    income = {
        "amount": amount,
        "source": source
    }

    income_data.append(income)

    return {
        "message": "Income Added Successfully",
        "data": income
    }


@router.get("/income")
def get_income():
    return income_data